<template>
  <div class="add-new-product-page">
    <header-component />
    <el-input placeholder="Please input" v-model="input"></el-input>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
export default {
  data() {
    return {
      input: "",
    };
  },
  components: {
    HeaderComponent,
  },
};
</script>

<style lang="scss">
.add-new-product-page {
}
</style>