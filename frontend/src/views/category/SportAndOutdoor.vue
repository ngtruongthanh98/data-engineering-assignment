<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Sport & Outdoor"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { SPORT_AND_OUTDOOR } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: SPORT_AND_OUTDOOR,
    };
  },
  components: {
    HeaderComponent,
    SubCategoryComponent,
  },
};
</script>

<style lang="scss">
.category {
}
</style>