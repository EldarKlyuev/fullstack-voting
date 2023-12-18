<template>
  <q-layout class="app-layout" view="lHr LpR lFf">
    <!-- <app-pages-drawer class="app-layout__drawer" />
    <app-header class="app-layout__header" /> -->
    <q-page-container class="app-layout__page-container">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
// import AppHeader from 'src/components/the/AppHeader.vue'
// import AppPagesDrawer from 'src/components/the/AppPagesDrawer.vue'
// import { storeToRefs } from 'pinia'

</script>

<style lang="scss">
.app-layout {
  &__page-container {
    height: 0px;
  }
}
</style>
