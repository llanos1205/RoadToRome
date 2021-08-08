<template>
<div  style="width: 100%">
    <input type="text" placeholder="Search..." v-model="searchQuery"/>
    <i class="search icon"></i>
  </div>
  <div  style="margin: 10px">
    <div
      
      v-for="wall in searchedProducts"
      :key="wall.id"
      style="margin: 0"
    >
      <div class="content">
        <div class="header">{{ wall.origin }}</div>
        <div class="meta">
          {{ wall.origin }} | {{ wall.destination }} |
          {{ wall.destination }} 
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { computed, ref,reactive } from "vue";
export default {
  name: "Walls",
  setup() {
    // make users variable reactive with the ref() functi on
    const walls = reactive([]);
    
    const searchQuery = ref("");
    const searchedProducts = computed(() => {
      return walls.value.filter((wall) => {
        return (
          wall.origin
            .toLowerCase()
            .indexOf(searchQuery.value.toLowerCase()) != 1
        );
      });
});
    return {
      searchedProducts, searchQuery
    };
  },

  async mounted() {
    await axios.get("/core/wall", {}).then((res) => {
      this.walls = res.data;
    });
  },
};
</script>