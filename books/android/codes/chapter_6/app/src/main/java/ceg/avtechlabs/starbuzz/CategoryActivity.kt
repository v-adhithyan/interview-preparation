package ceg.avtechlabs.starbuzz

import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter

import kotlinx.android.synthetic.main.activity_drink.*

class CategoryActivity : AppCompatActivity(), AdapterView.OnItemClickListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_drink)

        val adapter = ArrayAdapter<Drink>(this@CategoryActivity, android.R.layout.simple_list_item_1,
                Drink.drinks)
        list_drinks.adapter = adapter
        list_drinks.setOnItemClickListener(this)
    }

    override fun onItemClick(p0: AdapterView<*>?, p1: View?, p2: Int, id: Long) {
        val intent = Intent(this@CategoryActivity, DrinkActivity::class.java)
        intent.putExtra(EXTRA_DRINKNO, id)
        startActivity(intent)
    }

    companion object {
        val EXTRA_DRINKNO = "dno"
    }
}

