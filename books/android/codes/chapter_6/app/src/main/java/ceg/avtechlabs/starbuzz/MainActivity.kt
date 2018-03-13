package ceg.avtechlabs.starbuzz

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity(), AdapterView.OnItemClickListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        list_options.setOnItemClickListener(this)
    }

    override fun onItemClick(parent: AdapterView<*>?, view: View?, pos: Int, id: Long) {
        when (pos) {
            0 -> {startActivity(Intent(this@MainActivity, CategoryActivity::class.java))}
            1 -> {startActivity(Intent(this@MainActivity, DrinkActivity::class.java))}
            2 -> {startActivity(Intent(this@MainActivity, StoresActivity::class.java))}
        }
    }

}
