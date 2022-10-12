<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="sub-category-list">
    <div class="sub-category">
      <span><i class="el-icon-menu"></i> </span> All Sub-Categories
    </div>

    <div class="title">
      <span><i class="el-icon-caret-right"></i></span> {{ title }}
    </div>

    <div
      v-for="(item, index) in subCategoryList"
      :key="index"
      class="sub-category-item"
    >
      {{ item }}
    </div>
  </div>
</template>

<script>
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
};
</script>

<style lang="scss">
.sub-category-list {
  width: 190px;
  text-align: left;

  .sub-category {
    font-size: 16px;
    text-transform: capitalize;
    text-decoration: none;
    color: rgba(0, 0, 0, 0.8);
    height: 3.125rem;
    line-height: 3.125rem;
    font-weight: 700;
    font-size: 1rem;
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    margin-bottom: 0.625rem;
  }

  .sub-category-item {
    padding: 0.5rem 0.625rem 0.5rem 0.75rem;
    transition: opacity 0.2s ease;

    &:hover {
      color: $color-primary;
      cursor: pointer;
    }
  }
}
</style>