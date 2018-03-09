package ceg.avtechlabs.beeradviser

/**
 * Created by Adhithyan V on 08-03-2018.
 */

class BeerExpert() {
    fun getBrands(color: String): List<String> {
        val brands = ArrayList<String>()

        when (color) {
            "amber" -> { brands.add("Jack Amber")
                brands.add("Red Moose")}
            else -> {
                brands.add("Jail Pale Ale")
                brands.add("Gout Stout")
            }
        }

        return brands
    }
}