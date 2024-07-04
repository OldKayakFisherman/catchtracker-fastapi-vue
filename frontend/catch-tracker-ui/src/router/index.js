import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import AddCatchView from '../views/AddCatchView.vue'
import CatchView from '../views/CatchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: 'home',
      component: IndexView
    },
    {
      path: '/addcatch',
      name: 'addcatch',
      component: AddCatchView
    },
    {
      path: '/viewcatches',
      name: 'viewcatches',
      component: CatchView
    },
  ]
})

export default router
