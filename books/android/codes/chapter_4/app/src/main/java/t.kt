import android.os.Handler

/**
 * Created by Adhithyan V on 08-03-2018.
 */

class t {
    fun temp() {
        val handler = Handler()
        handler.post(object : Runnable {
            override fun run() {
                handler.postDelayed(this, 1000)
            }
        })
    }
}
