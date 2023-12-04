<template>
  <div id="app">
    <poll-form />
    <poll-list />
  </div>
</template>

<script>
import PollForm from './components/PollForm.vue';
import PollList from './components/PollList.vue';

export default {
  components: {
    PollForm,
    PollList
  }
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 2rem;
}

h2 {
  margin-bottom: 1rem;
}
</style>
