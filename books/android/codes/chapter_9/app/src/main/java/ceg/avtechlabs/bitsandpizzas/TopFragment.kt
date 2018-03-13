package ceg.avtechlabs.bitsandpizzas


import android.os.Bundle
import android.app.Fragment
import android.app.ListFragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup


/**
 * A simple [Fragment] subclass.
 */
class TopFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup, savedInstanceState: Bundle?): View {
        return inflater.inflate(R.layout.fragment_top, container, false)
    }

}// Required empty public constructor
