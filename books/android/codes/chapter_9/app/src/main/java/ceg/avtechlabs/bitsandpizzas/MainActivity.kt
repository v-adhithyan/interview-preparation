package ceg.avtechlabs.bitsandpizzas

import android.app.Activity
import android.app.Fragment
import android.app.FragmentTransaction
import android.content.Intent
import android.os.Bundle
import android.support.v4.app.ActionBarDrawerToggle
import android.view.Gravity
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.ListView
import android.widget.ShareActionProvider
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : Activity(), AdapterView.OnItemClickListener {
    var shareActionProvider: ShareActionProvider? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        drawer_layout.openDrawer(Gravity.START)
        val titles = resources.getStringArray(R.array.titles)
        drawer.adapter = ArrayAdapter<String>(this, android.R.layout.simple_list_item_activated_1, titles)
        drawer.setOnItemClickListener(this)

        var drawerToggle = ActionBarDrawerToggle(this, drawer_layout, -1, R.string.open_d, R.string.close_d)

    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        val menuItem = menu?.findItem(R.id.menu_share)
        if (menuItem != null) {
            shareActionProvider = menuItem?.actionProvider as ShareActionProvider
            setIntent("Adhithyan")
        }
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        when (item?.itemId) {
            (R.id.menu_new_order) -> {startActivity(Intent(this@MainActivity, OrderActivity::class.java))}
            (R.id.menu_settings) -> {}
        }
        return true
    }

    fun setIntent(text: String) {
        val intent = Intent(Intent.ACTION_SEND)
        intent.type = "text/plain"
        intent.putExtra(Intent.EXTRA_TEXT, text)
        shareActionProvider?.setShareIntent(intent)
    }

    override fun onItemClick(p0: AdapterView<*>?, p1: View?, pos: Int, id: Long) {
        selectItem(pos)
    }

    fun selectItem(pos: Int) {
        var fragment: Fragment? = null

        when(pos) {
            (1) -> fragment = PizzaFragment()
            (2) -> fragment = PastaFragment()
            (3) -> fragment = StoresFragment()
            else -> fragment = TopFragment()
        }

        val ft = fragmentManager.beginTransaction()
        ft.replace(R.id.content_frame, fragment)
        ft.addToBackStack(null)
        ft.setTransition(FragmentTransaction.TRANSIT_FRAGMENT_FADE)
        ft.commit()
    }


}
