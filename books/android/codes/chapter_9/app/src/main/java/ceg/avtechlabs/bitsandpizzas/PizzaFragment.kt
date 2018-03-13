package ceg.avtechlabs.bitsandpizzas


import android.app.ListFragment
import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.TextView


/**
 * A simple [Fragment] subclass.
 */
class PizzaFragment : ListFragment() {


    override fun onCreateView(inflater: LayoutInflater?, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        val adapter = ArrayAdapter<String>(inflater?.context, android.R.layout.simple_list_item_1, resources.getStringArray(R.array.pizzas))

        listAdapter = adapter

        return super.onCreateView(inflater, container, savedInstanceState)
    }

}// Required empty public constructor
