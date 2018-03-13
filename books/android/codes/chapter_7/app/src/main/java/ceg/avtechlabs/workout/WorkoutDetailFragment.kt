package ceg.avtechlabs.workout


import android.app.Fragment
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.fragment_workout_detail.*


/**
 * A simple [Fragment] subclass.
 */
class WorkoutDetailFragment : Fragment() {

    var workoutId = 0L

    override fun onCreateView(inflater: LayoutInflater?, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment

        if(savedInstanceState != null) {
            workoutId = savedInstanceState.getLong("id")
        }

        return inflater!!.inflate(R.layout.fragment_workout_detail, container, false)
    }

    override fun onStart() {
        super.onStart()

        if(view != null) {
            val workout = Workout.workouts[workoutId.toInt()]
            title_text.text = workout.name
            description_text.text = workout.description
        }
    }

    override fun onSaveInstanceState(outState: Bundle?) {
        super.onSaveInstanceState(outState)
        outState?.putLong("id", workoutId)
    }

}// Required empty public constructor

