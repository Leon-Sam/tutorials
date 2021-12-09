import { makeExecutableSchema } from "@graphql-tools/schema";
import typeDefs from "./schema.graphql";
import { GraphQLContext } from "./context";
import { Link } from ".prisma/client";
import { APP_SECRET } from "./auth";
import { compare, hash } from "bcryptjs";
import {sign} from "jsonwebtoken";
import { ExecutionArgs } from "graphql";
const resolvers = {
    Query: {
      info: () => `This is the API of a Hackernews Clone`,
      feed: async (parent:unknown, args:{},context:GraphQLContext)=>{
        return context.prisma.link.findMany();
      },
      me: (parent:unknown,args:{},context:GraphQLContext)=>{
        if (context.currentUser===null){
          throw new Error("Unauthenicated");
        }

        return context.currentUser;
      }
    },
    Link: {
      id: (parent: Link) => parent.id,
      description: (parent: Link) => parent.description,
      url: (parent: Link) => parent.url,
    },
    Mutation: {
      post: async (parent: unknown, 
             args: { description: string, url: string },
             context:GraphQLContext) => {
        // 1
        const newLink= context.prisma.link.create({
          data:{
            url:args.url,
            description:args.description
          }
        })

  
        return newLink;
      },
      signup: async (
        parent:unknown,
        args:{
            email:string;
            password:string;
            name:string;
        },
        context:GraphQLContext
      )=>{
          const password = await hash(args.password,10);

          const user = await context.prisma.user.create({
            data:{...args,password}
          });

          const token = sign({userId:user.id},APP_SECRET);

          return {
            token,
            user
          }

      },
      login: async (
        parent: unknown,
        args: {email:string,password:string},
        context:GraphQLContext
      )=>{
        const user = await context.prisma.user.findUnique({
          where:{email:args.email},
        });

        if (!user){
          throw new Error("No such found user")
        }

        const valid =await compare(args.password,user.password);

        if(!valid){
          throw new Error ("Invalid password");
        }

        const token =sign({userId:user.id},APP_SECRET)


        return {
          token,
          user
        }
      }
    },
  };

export const schema = makeExecutableSchema({
  typeDefs,
  resolvers,
});