package com.example.myfirstapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class DisplayMessageActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_message);

        //Get the intent that started activity
        Intent intent = getIntent();
        String message= intent.getStringExtra(MainActivity.EXTRA_MESSAGE);

        //Capture textview layout
        TextView textView = findViewById(R.id.textView);
        textView.setText(message);

    }

}