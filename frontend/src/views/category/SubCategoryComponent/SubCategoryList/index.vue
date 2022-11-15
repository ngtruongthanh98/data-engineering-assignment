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
      :class="
        item.subcategoryName === selectedSubCategory
          ? 'sub-category-item selected'
          : 'sub-category-item'
      "
      @click="selectSubCategory(item.subcategoryName)"
    >
      {{ item.subcategoryName }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedSubCategory: this.subCategoryList[0]?.subcategoryName,
    };
  },
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
  methods: {
    selectSubCategory(subCategoryName) {
      this.selectedSubCategory = subCategoryName;
      this.$emit("select-subcategory", subCategoryName);
    },
  },
  mounted() {
    console.log("selectedSubCategory: ", this.selectedSubCategory);
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
    color: $color-border-sub-category;
    height: 3.125rem;
    line-height: 3.125rem;
    font-weight: 700;
    font-size: 1rem;
    border-bottom: 1px solid $color-border-sub-category-2;
    margin-bottom: 0.625rem;
  }

  .sub-category-item {
    padding: 0.5rem 0.625rem 0.5rem 0.75rem;
    transition: opacity 0.2s ease;

    &:hover {
      color: $color-primary;
      cursor: pointer;
    }

    &.selected {
      color: $color-primary;
    }
  }
}
</style>