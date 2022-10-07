<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="sub-category-container">
    <h1 class="title">{{ title }}</h1>

    <div class="body">
      <sub-category-list :title="title" :subCategoryList="subCategoryList" />
    </div>
  </div>
</template>

<script>
import SubCategoryList from "./SubCategoryList";

export default {
  props: {
    title: {
      type: String,
      default: "",
    },
    subCategoryList: {
      type: Array,
      default: () => [],
    },
  },
  components: {
    SubCategoryList,
  },
};
</script>

<style lang="scss">
.sub-category-container {
  .title {
    padding: 0.5rem 0.625rem 0.5rem 0.75rem;
  }
  .body {
    font-size: 14px;
  }
}
</style>