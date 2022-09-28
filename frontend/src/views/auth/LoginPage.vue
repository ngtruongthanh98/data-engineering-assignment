<template>
  <div class="login-page">
    <h1>Login Page</h1>

    <el-form
      :label-position="labelPosition"
      label-width="100px"
      :model="loginForm"
    >
      <el-form-item label="Username">
        <el-input v-model="loginForm.username"></el-input>
      </el-form-item>
      <el-form-item label="Password">
        <el-input v-model="loginForm.password" type="password"></el-input>
      </el-form-item>

      <el-link href="http://localhost:8080/forgot-password"
        >Forgot password?</el-link
      >
      <el-link href="http://localhost:8080/register">Register</el-link>

      <el-form-item>
        <el-button type="primary" @click="submitForm('dynamicValidateForm')"
          >Login</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "LoginPage",
  components: {},
  data() {
    return {
      input: "",
      labelPosition: "right",
      loginForm: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    submitForm(loginForm) {
      console.log(loginForm);
    },
  },
};
</script>