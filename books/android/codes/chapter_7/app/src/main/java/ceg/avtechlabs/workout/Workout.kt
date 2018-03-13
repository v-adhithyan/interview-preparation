package ceg.avtechlabs.workout

/**
 * Created by Adhithyan V on 09-03-2018.
 */

data class Workout(val name: String, val description: String) {

    companion object {
        val workouts = arrayOf(
                Workout("The limb loosener", "5 pushups\n10 1-legged squats\n15 Pullups"),
                Workout("Core Agony", "100 Pullups\n100 pushups\n100 situps"),
                Workout("The wimp special", "5 pullups\n10 pushups\n15 squats"),
                Workout("Strength and length", "500 meter run\n21 x pullups")
        )
    }

    override fun toString(): String {
        return name
    }
}