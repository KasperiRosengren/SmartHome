package com.project.test_again_kotlin

// import android.view.ViewGroup
// import android.widget.Button
// import android.widget.LinearLayout
// alla olevalla saa siistittyä koodia mutta vaatii puukkoa moduliin, duunaaduunaa
// import android.os.AsyncTask

// olisiko java.URLConnection parempi...
import android.content.Context
import java.net.URLConnection

import android.content.Intent
import android.os.AsyncTask
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.activity_mqttactivity.*
import okhttp3.OkHttpClient
import java.io.BufferedInputStream
import java.io.InputStream
import java.net.HttpURLConnection
import java.net.URL

// katsotaan okhttp librarya
/*
import okhttp3.Call
import okhttp3.Callback
import okhttp3.FormBody
import okhttp3.MediaType
import okhttp3.Request
import okhttp3.RequestBody */

// vaihtoehtoisesti ktor, kotlin tekijöiltä
import io.ktor.client.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.http.*
import io.ktor.client.engine.android.*
import org.json.JSONObject
import java.net.InetSocketAddress
import java.net.Proxy

// import io.ktor.client.engine.cio.*



class LoginActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        // text kentät ja muuttujat
        var omaLoginUserName = editTextLoginUsername.text.toString()
        var omaLoginPassword = editTextLoginPassword.text.toString()
        var loginServeriIP = editTextLoginServerIP.text.toString()
        var loginServeriPort = editTextLoginServerPort.text.toString()
        var myLoginOsoite = "" + loginServeriIP + ":" + loginServeriPort + ""
        var textViewLoginDebug = findViewById(R.id.textViewLoginDebug) as TextView

        // ktor alustukseen liittyvät
        val OmaClient = HttpClient(Android) {
            engine {
                // this: AndroidEngineConfig
                connectTimeout = 100_000
                socketTimeout = 100_000
                proxy = Proxy(Proxy.Type.HTTP, InetSocketAddress("localhost", 8080))
            }




        HttpClient() {
            engine {
                // this: HttpClientEngineConfig
                threadsCount = 4
                pipelining = true
            }
        }
        // ktor luodaan response muuttuja
       // val response: HttpResponse = OmaClient.request("https://ktor.io/") {
       //     method = HttpMethod.Get
        }

        // kokeilussa urlGET URLConnection librarystä
        val urlGET = "https://ktor.io/"
        //GET Request
        NetworkAsyncCall(this@LoginActivity, urlGET, RequestHandler.GET).execute();

        //       POST Request
        //        doPost()


        // kirjautumisnappula
        val buttonLogin = findViewById<Button>(R.id.buttonLogin)

        // duunaaduunaa testataan okhttp kirjastolla http yhteyttä
        var client = OkHttpClient()
        var request = OkHttpRequest(client)
        // debug app ruutuun:
        fun kirjoitaAppDebug() {
            // finding the textView
            //    Toast.makeText(this@LoginActivity, "Osoite: " + myLoginOsoite + "", Toast.LENGTH_LONG).show()
            textViewLoginDebug.text =
                "Osoite: " + myLoginOsoite + "\nUsername: " + omaLoginUserName + "\nPassword xD :" + omaLoginPassword + ""
        }
        fun postaa() { // (url: String, parameters: HashMap<String, String>, callback: Callback): Call {
    /*
            val builder = FormBody.Builder()
            val it = parameters.entries.iterator()
            while (it.hasNext()) {
                val pair = it.next() as Map.Entry<*, *>
                builder.add(pair.key.toString(), pair.value.toString())
            }

            val formBody = builder.build()
            val request = Request.Builder()
                .url(url)
                .post(formBody)
                .build()


            val call = client.newCall(request)
            call.enqueue(callback)
            return call

   */
        }


        fun readStream(inputStream: InputStream) {
            /*
            val url = URL(myLoginOsoite)
            val urlConnection: HttpURLConnection = url.openConnection() as HttpURLConnection
            try {
                val `in`: InputStream = BufferedInputStream(urlConnection.getInputStream())
                readStream(`in`)
                Toast.makeText(this@LoginActivity, "connecting" + myLoginOsoite +"", Toast.LENGTH_SHORT).show()
            } finally {
                urlConnection.disconnect()
            }

         */
        }



        fun luoLoginStringgi() {

           // ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.INTERNET}, 0);
          /*  http://localhost:5000/api/auth/login POST

            {

                "username": "INSERTYOURUSERNAMEHERE", "password": "INSERTYOURPASSWORDHERE"

            }

            http://localhost:5000/api/get/frontend/test/init GET */

        }



        // aloitetaan login proceduuri painettaessa Login nappulaaaaaa

        buttonLogin?.setOnClickListener()
        {
            //Toast.makeText(this@LoginActivity, R.string.message_get_login, Toast.LENGTH_LONG).show()
            // vaihda zone activity tai laite act alle
            // val intent = Intent(this@LoginActivity, ClassRunLogin::class.java)
            // startActivity(intent)


            kirjoitaAppDebug()
         //   readStream()
          //  postaa(myLoginOsoite, "jaahas")
            val response: String = "Lennosta luotu testi" //OmaClient.get("https://ktor.io/")
            Toast.makeText(this@LoginActivity, response, Toast.LENGTH_SHORT).show()
        }

        // reset nappula
        buttonResetLogin?.setOnClickListener() {
          editTextLoginUsername.setText("")
            editTextLoginPassword.setText("")
           // ut_username = ""
          omaLoginPassword  = ""
          omaLoginUserName = ""
        }
        // tässä vaiheessa mennään tavallisella buttonilla, vaihdetaan floating myöhemmin

        val buttonGoToMain = findViewById<Button>(R.id.buttonGoToMain)
            buttonGoToMain?.setOnClickListener(){
                val intent = Intent(this@LoginActivity, MainActivity::class.java)
                startActivity(intent)

            }
      /*  val fabToMain = findViewById<FloatingActionButton>(R.id.fabToMain)

        fabToMain.setOnClickListener { /* view ->
            Snackbar.make(view, "Takaisin päävalikkoon", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show() */


            val intent = Intent(this@LoginActivity, MainActivity::class.java)
            startActivity(intent)

        } */
      fun execute() {
          TODO("Not yet implemented")
          Toast.makeText(this@LoginActivity, "tässä on oma execute teksti", Toast.LENGTH_SHORT).show()
      }

    }
    // ----------------------------------  Testaa URLConnection ------------------
    class NetworkAsyncCall(private val context: Context, private val url: String, private val requestType:
    String, private val postJSONObject: JSONObject = JSONObject()
    ) : AsyncTask<String?, String?, String?>() {

        override fun doInBackground(vararg p0: String?): String? {
            return when (requestType) {
                RequestHandler.GET -> RequestHandler.requestGET(url)
                RequestHandler.GET -> RequestHandler.requestPOST(url, postJSONObject)
                else -> ""
            }
        }

        override fun onPostExecute(s: String?) {
            if (s != null) {
                Toast.makeText(context, s, Toast.LENGTH_LONG).show()
            }
        }


    }
}

