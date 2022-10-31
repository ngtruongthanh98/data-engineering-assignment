<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Mobile & Gadgets"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { MOBILE_AND_GADGETS } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: MOBILE_AND_GADGETS,
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