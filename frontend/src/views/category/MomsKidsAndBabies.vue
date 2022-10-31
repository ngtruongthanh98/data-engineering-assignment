<template>
  <div class="category">
    <header-component />

    <sub-category-component
      title="Moms, Kids and Babies"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { MOMS_KIDS_AND_BABIES } from "@/constants";

export default {
  data() {
    return {
      subCategoryList: MOMS_KIDS_AND_BABIES,
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