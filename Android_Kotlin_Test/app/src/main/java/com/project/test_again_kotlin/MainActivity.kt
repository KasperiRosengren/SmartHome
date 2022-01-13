package com.project.test_again_kotlin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // laitetaan tämä siirtymään login activity
        val buttonGoToLogin  = findViewById<Button>(R.id.buttonGoToLogin)
        // button siirry tabbed everything activitettiin
        val buttonGoToEverything = findViewById<Button>(R.id.buttonGoToEverything)
        // mennään laiteluetteloon
        val buttonGoToDevices  = findViewById<Button>(R.id.buttonGoToDevices)
        //duunaaduunaa lisätään button joka siirtyy suoraan zoneihin tms

        // button  siirrytään MQTT main sivulle
        val buttonGoToMQTTActivity = findViewById<Button>(R.id.buttonGoMQTT)

        // kuuntelija GoToLogin buttonille
        buttonGoToLogin?.setOnClickListener()
        {
            Toast.makeText(this@MainActivity, R.string.messageGoToLogin, Toast.LENGTH_LONG).show()
            val intent = Intent(this@MainActivity, LoginActivity::class.java)
            startActivity(intent)
        }
        buttonGoToEverything?.setOnClickListener()
        {
            Toast.makeText(this@MainActivity, R.string.messageGoToEverything, Toast.LENGTH_LONG).show()
            val intent = Intent(this@MainActivity, ShowEverythingActivity::class.java)
            startActivity(intent)
        }

        buttonGoToDevices?.setOnClickListener()
        {
            Toast.makeText(this@MainActivity, R.string.messageGoToDevices, Toast.LENGTH_LONG).show()
            val intent = Intent(this@MainActivity, ShowDevicesActivity::class.java)
            startActivity(intent)
        }
        buttonGoToMQTTActivity?.setOnClickListener()
        {
            Toast.makeText(this@MainActivity, R.string.messageGoToMQTT, Toast.LENGTH_LONG).show()
            val intent = Intent(this@MainActivity, MQTTActivity::class.java)
            startActivity(intent)
        }
    }
}
