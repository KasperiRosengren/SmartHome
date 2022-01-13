package com.project.test_again_kotlin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
// import android.view.ViewGroup
// import android.widget.Button
// import android.widget.LinearLayout
import android.widget.Toast
// alla olevalla saa siistittyä koodia mutta vaatii puukkoa moduliin, duunaaduunaa
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.activity_show_devices.*

class ShowDevicesActivity : AppCompatActivity(){

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_show_devices)


       val buttonGetDevices  = findViewById<Button>(R.id.buttonGetDevices)
       val buttonRefreshDevices =  findViewById<Button>(R.id.buttonRefreshDevices)
        // info/statusruutu
        val textViewStatus = findViewById(R.id.textViewStatus) as TextView

        //duunaaduunaa lisätään button joka siirtyy suoraan zoneihin tms

        // kuuntelija ekalle buttonille
       //val buttonGetDevices = findViewById<Button>(R.id.buttonGetDevices)
       buttonGetDevices?.setOnClickListener()
        {
            // näytetään nyt vaan jotain (toast message tässä tapauksessa
            // Toast.makeText(this@MainActivity, R.string.messageGoToLogin, Toast.LENGTH_LONG).show()
            // vaihda zone activity tai laite act alle
            // val intent = Intent(this@ShowDevicesActivity, LoginActivity::class.java)
            // startActivity(intent)
            textViewStatus.text = "Haetaan laiteluetteloa"

        }

        buttonRefreshDevices?.setOnClickListener()
        {
            // näytetään nyt vaan jotain (toast message tässä tapauksessa
            // Toast.makeText(this@MainActivity, R.string.messageGoToLogin, Toast.LENGTH_LONG).show()
            // vaihda zone activity tai laite act alle
            // val intent = Intent(this@ShowDevicesActivity, LoginActivity::class.java)
            // startActivity(intent)
           // Toast.makeText(textViewStatus, "Päivitetään laiteluetteloa", Toast.LENGTH_SHORT)
           //     .show()
            textViewStatus.text = "Päivitetään laiteluetteloa"
        }
        // inforuutu
        //textViewStatus?.setOnClickListener{ Toast.makeText(this@ShowDevicesActivity,
         //   "StatusRuutu katso toiminto", Toast.LENGTH_LONG).show() }


    }
}
