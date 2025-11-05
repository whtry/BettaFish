# -*- coding: utf-8 -*-
"""
微舆配置文件（整合本地化配置）

此模块使用 pydantic-settings 管理全局配置，支持从环境变量和 .env 文件自动加载，
同时保留本地Ollama和SearXNG的配置方案。
"""

from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


# 计算 .env 优先级：优先当前工作目录，其次项目根目录
PROJECT_ROOT: Path = Path(__file__).resolve().parent
CWD_ENV: Path = Path.cwd() / ".env"
ENV_FILE: str = str(CWD_ENV if CWD_ENV.exists() else (PROJECT_ROOT / ".env"))


class Settings(BaseSettings):
    """
    全局配置；支持 .env 和环境变量自动加载，整合本地Ollama配置。
    """
    
    # ====================== 数据库配置 ======================
    DB_DIALECT: str = Field("mysql", description="数据库类型，例如 'mysql' 或 'postgresql'")
    DB_HOST: str = Field("mysql", description="数据库主机，本地默认使用mysql容器")
    DB_PORT: int = Field(3306, description="数据库端口号")
    DB_USER: str = Field("root", description="数据库用户名，本地默认root")
    DB_PASSWORD: str = Field("local_password", description="数据库密码，本地默认密码")
    DB_NAME: str = Field("mindspider", description="数据库名称，本地默认mindspider")
    DB_CHARSET: str = Field("utf8mb4", description="数据库字符集，推荐utf8mb4")
    
    # ======================= Ollama 基础配置 =======================
    OLLAMA_BASE_URL: str = Field("http://ollama:11434/v1", description="本地Ollama服务地址")
    
    # ======================= LLM 相关（基于Ollama） =======================
    # Insight Agent（使用本地Ollama）
    INSIGHT_ENGINE_API_KEY: str = Field("ollama", description="Ollama无需实际API密钥")
    INSIGHT_ENGINE_BASE_URL: str = Field(OLLAMA_BASE_URL, description="Insight Agent使用Ollama服务地址")
    INSIGHT_ENGINE_MODEL_NAME: str = Field("qwen3:30b", description="Ollama中的qwen3:30b模型")
    
    # Media Agent（使用本地Ollama）
    MEDIA_ENGINE_API_KEY: str = Field("ollama", description="Ollama无需实际API密钥")
    MEDIA_ENGINE_BASE_URL: str = Field(OLLAMA_BASE_URL, description="Media Agent使用Ollama服务地址")
    MEDIA_ENGINE_MODEL_NAME: str = Field("qwen3:30b", description="Ollama中的qwen3:30b模型")
    
    # Query Agent（使用本地Ollama）
    QUERY_ENGINE_API_KEY: str = Field("ollama", description="Ollama无需实际API密钥")
    QUERY_ENGINE_BASE_URL: str = Field(OLLAMA_BASE_URL, description="Query Agent使用Ollama服务地址")
    QUERY_ENGINE_MODEL_NAME: str = Field("qwen3:30b", description="Ollama中的qwen3:30b模型")
    
    # Report Agent（使用本地Ollama）
    REPORT_ENGINE_API_KEY: str = Field("ollama", description="Ollama无需实际API密钥")
    REPORT_ENGINE_BASE_URL: str = Field(OLLAMA_BASE_URL, description="Report Agent使用Ollama服务地址")
    REPORT_ENGINE_MODEL_NAME: str = Field("qwen3:30b", description="Ollama中的qwen3:30b模型")
    
    # Forum Host（使用本地Ollama）
    FORUM_HOST_API_KEY: str = Field("ollama", description="Ollama无需实际API密钥")
    FORUM_HOST_BASE_URL: str = Field(OLLAMA_BASE_URL, description="Forum Host使用Ollama服务地址")
    FORUM_HOST_MODEL_NAME: str = Field("qwen3:30b", description="Ollama中的qwen3:30b模型")
    
    # SQL keyword Optimizer（使用本地Ollama）
    KEYWORD_OPTIMIZER_API_KEY: str = Field("ollama", description="Ollama无需实际API密钥")
    KEYWORD_OPTIMIZER_BASE_URL: str = Field(OLLAMA_BASE_URL, description="Keyword Optimizer使用Ollama服务地址")
    KEYWORD_OPTIMIZER_MODEL_NAME: str = Field("qwen3:30b", description="Ollama中的qwen3:30b模型")
    
    # ================== 网络工具配置（使用SearXNG） ====================
    SEARXNG_URL: str = Field("http://searxng:8888", description="本地SearXNG服务地址")
    
    # Tavily替换为SearXNG
    TAVILY_API_KEY: str = Field("local", description="本地SearXNG无需实际密钥")
    TAVILY_BASE_URL: str = Field(f"{SEARXNG_URL}/search", description="SearXNG搜索接口地址")
    
    # Bocha替换为SearXNG
    BOCHA_BASE_URL: str = Field(f"{SEARXNG_URL}/search", description="SearXNG搜索接口地址（替代博查）")
    BOCHA_WEB_SEARCH_API_KEY: str = Field("local", description="本地SearXNG无需实际密钥")
    
    # ================== Insight Engine 搜索配置 ====================
    DEFAULT_SEARCH_HOT_CONTENT_LIMIT: int = Field(100, description="热榜内容默认最大数")
    DEFAULT_SEARCH_TOPIC_GLOBALLY_LIMIT_PER_TABLE: int = Field(50, description="按表全局话题最大数")
    DEFAULT_SEARCH_TOPIC_BY_DATE_LIMIT_PER_TABLE: int = Field(100, description="按日期话题最大数")
    DEFAULT_GET_COMMENTS_FOR_TOPIC_LIMIT: int = Field(500, description="单话题评论最大数")
    DEFAULT_SEARCH_TOPIC_ON_PLATFORM_LIMIT: int = Field(200, description="平台搜索话题最大数")
    MAX_SEARCH_RESULTS_FOR_LLM: int = Field(0, description="供LLM用搜索结果最大数")
    MAX_HIGH_CONFIDENCE_SENTIMENT_RESULTS: int = Field(0, description="高置信度情感分析最大数")
    MAX_REFLECTIONS: int = Field(3, description="最大反思次数")
    MAX_PARAGRAPHS: int = Field(6, description="最大段落数")
    SEARCH_TIMEOUT: int = Field(240, description="单次搜索请求超时")
    MAX_CONTENT_LENGTH: int = Field(500000, description="搜索最大内容长度")
    
    class Config:
        env_file = ENV_FILE
        env_prefix = ""
        case_sensitive = False
        extra = "allow"


# 创建全局配置实例
settings = Settings()
