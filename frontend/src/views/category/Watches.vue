<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />
    <div>Watches</div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";

export default {
  components: {
    HeaderComponent,
  },
};
</script>

<style lang="scss">
.category {
}
</style>
