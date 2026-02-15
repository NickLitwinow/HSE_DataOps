# Helm Chart — nginx

Helm-чарт для развертывания nginx веб-сервера в Kubernetes.

## Структура чарта

```
nginx-chart/
├── Chart.yaml                          # Метаданные чарта
├── values.yaml                         # Значения по умолчанию
├── .helmignore                         # Игнорируемые файлы
├── templates/
│   ├── _helpers.tpl                    # Вспомогательные шаблоны
│   ├── deployment.yaml                 # Шаблон Deployment
│   ├── service.yaml                    # Шаблон Service
│   └── ingress.yaml                    # Шаблон Ingress (опциональный)
└── examples/
    ├── values-minimal.yaml             # Минимальная конфигурация
    ├── values-staging.yaml             # Стейджинг конфигурация
    └── values-production.yaml          # Продакшн конфигурация
```

## Параметризация через шаблоны

| Параметр | Описание | По умолчанию |
|---|---|---|
| `image.repository` | Репозиторий образа | `nginx` |
| `image.tag` | Тег (версия) образа | `1.25-alpine` |
| `replicaCount` | Количество реплик | `3` |
| `resources.enabled` | Включить ресурсные лимиты | `true` |
| `resources.requests.memory` | Запрос памяти | `64Mi` |
| `resources.requests.cpu` | Запрос CPU | `100m` |
| `resources.limits.memory` | Лимит памяти | `128Mi` |
| `resources.limits.cpu` | Лимит CPU | `250m` |
| `ingress.enabled` | Генерировать манифест Ingress | `true` |
| `sharedMemory.enabled` | Увеличенный /dev/shm | `true` |
| `sharedMemory.sizeLimit` | Размер shared memory | `128Mi` |

## Примеры деплоя с разными настройками

### 1. Деплой по умолчанию

```bash
helm install nginx-default ./nginx-chart
```

### 2. Минимальный деплой (без ресурсов, без ingress)

```bash
helm install nginx-minimal ./nginx-chart -f examples/values-minimal.yaml
```

### 3. Стейджинг (nginx 1.24, уменьшенные ресурсы)

```bash
helm install nginx-staging ./nginx-chart -f examples/values-staging.yaml
```

### 4. Продакшн (5 реплик, увеличенные ресурсы)

```bash
helm install nginx-production ./nginx-chart -f examples/values-production.yaml
```

### 5. Переопределение через --set

```bash
helm install nginx-custom ./nginx-chart \
  --set image.tag="1.26-alpine" \
  --set replicaCount=4 \
  --set resources.enabled=false \
  --set ingress.enabled=false
```

## Проверка сгенерированных манифестов

```bash
# Просмотр итоговых манифестов без установки
helm template nginx-test ./nginx-chart

# Проверка с кастомными значениями
helm template nginx-test ./nginx-chart -f examples/values-minimal.yaml
```
