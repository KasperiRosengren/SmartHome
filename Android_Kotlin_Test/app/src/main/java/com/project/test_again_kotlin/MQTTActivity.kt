package com.project.test_again_kotlin

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

import android.widget.Button
import android.widget.Toast
import android.content.Intent
import android.os.AsyncTask
import android.view.View
import android.widget.EditText
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.activity_login.*
// alla olevalla saa siistittyä koodia mutta vaatii puukkoa moduliin, duunaaduunaa
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.activity_mqttactivity.*
import org.json.JSONObject


class MQTTActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_mqttactivity)


    var viesti = R.string.mqtt_subsripe_to_topic // muuttuja:topikin nimi"
    Toast.makeText(this@MQTTActivity, viesti, Toast.LENGTH_LONG).show()
    // vaihda zone activity tai laite act alle
    // val intent = Intent(this@LoginActivity, ClassRunLogin::class.java)
    // startActivity(intent)
    var serveriIP = editTextServerIP.text.toString()
    var serveriPortti = editTextServerPort.text.toString()
    var topikki = editTextTopikki.text.toString()
    var omaPayload = editTextPayload.text.toString()
    var incomingPayload = ""
    // val user_password = ut_password
    var kirjautumisStatus = "succes"
    var osoite = "" + serveriIP + ":" + serveriPortti +""
    var mqttKonteksti = applicationContext


    fun luoYhteys() {
        ClassMQTTConnection(mqttKonteksti ,osoite,"").connect(mqttKonteksti)
        }
    fun kirjauduTopikkiin() {
        ClassMQTTConnection(mqttKonteksti ,osoite,"").subscribe(topikki)
    }

    fun tarkistaStatus() {
    //    incomingPayload = ClassMQTTConnection(this.applicationContext).receiveMessages()

    }

/*
    var buttonMyMQTTPublish = findViewById<Button>(R.id.buttonMyMQTTPublish)
    buttonMyMQTTPublish?.setOnClickListener()
        {
            serveriIP = editTextServerIP.text.toString()
            serveriPortti = editTextServerPort.text.toString()
            topikki = editTextTopikki.text.toString()
            omaPayload = editTextPayload.text.toString()
            incomingPayload = ""
            // val user_password = ut_password
            kirjautumisStatus = "succes"
            osoite = "" + serveriIP + ":" + serveriPortti +""
            Toast.makeText(this@MQTTActivity, "topikki :" + topikki, Toast.LENGTH_SHORT).show()
            Toast.makeText(this@MQTTActivity, "ooite: " + osoite, Toast.LENGTH_SHORT).show()
       //     Toast.makeText(this@MQTTActivity, serveriPortti, Toast.LENGTH_SHORT).show()

       //     Toast.makeText(this@MQTTActivity, omaPayload, Toast.LENGTH_SHORT).show()
            luoYhteys()
            kirjauduTopikkiin()
            tarkistaStatus()

        }
        */

    }
}

