package ceg.avtechlabs.starbuzz

/**
 * Created by Adhithyan V on 09-03-2018.
 */

data class Drink(val name: String, val description: String, val resourceId: Int) {
    companion object {
        val drinks = arrayOf(
                Drink("Latte", "A couple of espresso shots with steamed milk", R.drawable.latte),
                Drink("Cappucino", "Espresso, hot milk and a steamed milk foam", R.drawable.cappuccino),
                Drink("Filter", "Highest quality beans roasted and brewed fresh", R.drawable.filter)
                )
    }

    override fun toString(): String {
        return name
    }
}