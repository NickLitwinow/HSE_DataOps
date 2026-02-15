{{/*
Полное имя ресурса
*/}}
{{- define "nginx-chart.fullname" -}}
{{- printf "%s-nginx" .Release.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Общие labels
*/}}
{{- define "nginx-chart.labels" -}}
app: {{ include "nginx-chart.fullname" . }}
chart: {{ .Chart.Name }}-{{ .Chart.Version }}
release: {{ .Release.Name }}
{{- end }}
