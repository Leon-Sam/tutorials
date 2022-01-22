import React from "react";
import { StyleSheet, View,ActivityIndicator } from "react-native";

export default function App() {
  const isLoading=true;


  return (<View style={styles.container}>

   <ActivityIndicator/>
  </View>);
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});