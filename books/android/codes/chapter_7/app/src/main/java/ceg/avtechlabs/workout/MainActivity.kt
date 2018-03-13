package ceg.avtechlabs.workout

import android.app.FragmentTransaction
import android.support.v7.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity(), WorkoutListFragment.WorkoutListener {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


    }

    override fun itemClicked(id: Long) {
        val details = WorkoutDetailFragment()
        details.workoutId = id

        val ft = fragmentManager.beginTransaction()
        ft.replace(R.id.fragment_container, details)
        ft.addToBackStack(null)

        ft.setTransition(FragmentTransaction.TRANSIT_FRAGMENT_FADE)
        ft.commit()
    }
}
