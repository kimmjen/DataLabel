<script setup>
import {ref} from 'vue'
import Upload from "./components/Upload.vue";

// 왼쪽 드로어 상태 관리
const leftDrawerOpen = ref(true)

// 드로어 토글 함수
const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
const model = ref(null);
</script>

<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
<!--        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer"/>-->

        <q-toolbar-title>
          <q-avatar>

          </q-avatar>
          Data Labeling Tools
        </q-toolbar-title>
      </q-toolbar>

<!--      <q-tabs align="left">-->
<!--        <q-route-tab to="/page1" label="Page One"/>-->
<!--        <q-route-tab to="/page2" label="Page Two"/>-->
<!--        <q-route-tab to="/page3" label="Page Three"/>-->
<!--      </q-tabs>-->
    </q-header>

<!--    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>-->
      <!-- drawer content -->
<!--    </q-drawer>-->

    <q-page-container>
      <Upload />
      <!--      <router-view />-->
    </q-page-container>

  </q-layout>
</template>


<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
