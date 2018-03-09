package ceg.avtechlabs.beeradviser

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun findBeer(v: View) {
        val selectedColor = color.selectedItem.toString()
        //brands.text = selectedColor

        val brandsList = BeerExpert().getBrands(selectedColor)
        val brandsFormatted = StringBuilder()
        for(brand in brandsList){
            brandsFormatted.append("$brand \n")
        }

        brands.text = brandsFormatted
    }
}
