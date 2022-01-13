package com.project.test_again_kotlin

import android.content.Intent
import android.os.Bundle
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import com.google.android.material.tabs.TabLayout
import androidx.viewpager.widget.ViewPager
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import com.project.test_again_kotlin.ui.main.SectionsPagerAdapter
import com.project.test_again_kotlin.databinding.ActivityShowEverythingBinding

class ShowEverythingActivity : AppCompatActivity() {

    private lateinit var binding: ActivityShowEverythingBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityShowEverythingBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val sectionsPagerAdapter = SectionsPagerAdapter(this, supportFragmentManager)
        val viewPager: ViewPager = binding.viewPager
        viewPager.adapter = sectionsPagerAdapter
        val tabs: TabLayout = binding.tabs
        tabs.setupWithViewPager(viewPager)
        val fabToMain: FloatingActionButton = binding.fabToMain

        fabToMain.setOnClickListener { view ->
            Snackbar.make(view, "Takaisin päävalikkoon", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show()


                    val intent = Intent(this@ShowEverythingActivity, MainActivity::class.java)
                    startActivity(intent)

        }
    }
}

