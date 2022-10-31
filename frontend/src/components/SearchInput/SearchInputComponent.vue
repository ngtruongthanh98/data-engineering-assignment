<template>
  <el-input placeholder="Type something" v-model="dataInput">
    <i slot="prefix" class="el-input__icon el-icon-search"></i>
  </el-input>
</template>

<script>
export default {
  data() {
    return {
      dataInput: "",
    };
  },
};
</script>

<style>
</style>