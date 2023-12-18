import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/AppPage.vue') }],
  },
  {
    path: '/add-poll',
    component: () => import('src/components/PollForm.vue')
  },
  {
    path: '/login',
    component: () => import('src/components/LoginComponent.vue')
  },
  {
    path: '/register',
    component: () => import('src/components/RegisterComponent.vue')
  }
];

export default routes;
