package ceg.avtechlabs.stopwatch

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    var running = false
    var seconds = 0
    var wasRunning: Boolean = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (savedInstanceState != null) {
            seconds = savedInstanceState.getInt("seconds")
            running = savedInstanceState.getBoolean("running")
            //wasRunning = savedInstanceState.getBoolean("wasRrunning")
        }

        startTimerLoop()
    }

    fun startWatch(v: View) {
        running = true
    }

    fun stopWatch(v: View) {
        running = false
    }

    fun resetWatch(v: View) {
        seconds = 0
    }

    fun runTimer() {
        val hours = seconds / 3600
        val minutes = (seconds % 3600) / 60
        val secs = seconds % 60

        val time = String.format("%d:%02d:%02d", hours, minutes, secs)
        time_view.text = time

        if (running) { seconds++ }
    }

    fun startTimerLoop() {
        val handler = Handler()
        handler.post(object : Runnable {
            override fun run() {
                runTimer()
                handler.postDelayed(this, 1000)
            }
        })
    }

    override fun onSaveInstanceState(outState: Bundle?) {
        super.onSaveInstanceState(outState)
        outState?.putInt("seconds", seconds)
        outState?.putBoolean("running", running)
    }

    override fun onStart() {
        super.onStart()
    }

    override fun onStop() {
        super.onStop()

        running = false
    }
}
