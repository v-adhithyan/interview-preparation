package ceg.avtechlabs.workout

import android.app.Activity
import android.app.ListFragment
import android.content.Context
import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.GridLayoutManager
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.ListView

import ceg.avtechlabs.workout.dummy.DummyContent
import ceg.avtechlabs.workout.dummy.DummyContent.DummyItem

/**
 * A fragment representing a list of Items.
 *
 *
 * Activities containing this fragment MUST implement the [OnListFragmentInteractionListener]
 * interface.
 */
/**
 * Mandatory empty constructor for the fragment manager to instantiate the
 * fragment (e.g. upon screen orientation changes).
 */
class WorkoutListFragment :  ListFragment() {

    // TODO: Customize parameters
    var listener: WorkoutListener? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

    }

    override fun onCreateView(inflater: LayoutInflater?, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        val view = inflater!!.inflate(R.layout.fragment_item_list, container, false)

        // Set the adapter
        val workouts = Workout.workouts
        val n = workouts.size
        val names = arrayOfNulls<String>(n)
        var i = 0
        for(w in workouts){
            names[i++] = w.name
        }
        listAdapter = ArrayAdapter<String>(inflater.context, android.R.layout.simple_list_item_1, names)

        return view
    }

    override fun onAttach(activity: Activity?) {
        super.onAttach(activity)
        this.listener = activity as WorkoutListener
    }

    override fun onListItemClick(l: ListView?, v: View?, position: Int, id: Long) {
        if(listener != null) {
            listener?.itemClicked(id)
        }
    }

    interface  WorkoutListener {
        fun itemClicked(id: Long);
    }

}
