package ceg.avtechlabs.starbuzz

import android.os.Bundle
import android.support.design.widget.Snackbar
import android.support.v7.app.AppCompatActivity

import kotlinx.android.synthetic.main.activity_food.*

class DrinkActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_food)

        val id = intent?.getLongExtra(CategoryActivity.EXTRA_DRINKNO, 0)!!.toInt()
        val drink = Drink.drinks[id]
        photo.setImageResource(drink.resourceId)
        name.text = drink.name
        description.text = drink.description
    }


}
