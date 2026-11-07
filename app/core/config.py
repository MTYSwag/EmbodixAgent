from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用配置：环境变量 / .env 读取，禁止提交真实密钥。"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "dev"
    version: str = "0.2.0"
    port: int = 9000
    llm_provider: str = "deepseek"  # deepseek | qwen | mock
    deepseek_api_key: str = ""
    qwen_api_key: str = ""

    @property
    def llm_key_configured(self) -> bool:
        if self.llm_provider == "mock":
            return True
        if self.llm_provider == "deepseek":
            return bool(self.deepseek_api_key)
        return bool(self.qwen_api_key)


settings = Settings()
