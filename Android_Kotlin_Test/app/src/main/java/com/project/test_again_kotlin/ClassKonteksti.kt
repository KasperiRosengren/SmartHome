package com.project.test_again_kotlin

import android.app.Application
import android.content.Context


class ClassKonteksti : Application() {
    override fun onCreate() {
        super.onCreate()
        application = this
    }

    companion object {
        var application: Application? = null
            private set
        val context: Context
            get() = application!!.applicationContext
    }
}