<template>
  <div class="user-avatar">
    <i class="el-icon-user"></i>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
.user-avatar {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background-color: $color-gray;

  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;

  .el-icon-user {
    font-size: 24px;
  }
}
</style>