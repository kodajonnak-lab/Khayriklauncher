KhayrikLauncher — пакет сборки настоящего Minecraft Java лаунчера

Это НЕ готовый APK. Пакет содержит настройки автоматической сборки APK на основе открытого проекта Amethyst-Android. APK появляется только после успешной сборки в GitHub Actions.

Содержимое: .github/workflows/build-launcher.yml — сценарий сборки; scripts/brand_upstream.py — меняет видимое имя приложения на KhayrikLauncher.

Загрузка с Android:
1. Распакуйте этот ZIP.
2. Загрузите в корень репозитория GitHub всё содержимое распакованной папки, включая скрытую папку .github и папку scripts. Не загружайте ZIP единственным файлом.
3. Убедитесь, что путь в репозитории выглядит так: .github/workflows/build-launcher.yml
4. Откройте Actions → Build KhayrikLauncher (Minecraft Java) → Run workflow.
5. Дождитесь зелёной галочки, откройте запуск и скачайте Artifact KhayrikLauncher-APK.
6. Распакуйте скачанный Artifact ZIP — внутри должен быть APK.

Если workflow не виден, проверьте, что .github/workflows/build-launcher.yml действительно загрузился, а Actions разрешены в репозитории.

Важно: workflow не запускался и APK не собран в этом чате, поэтому успешная сборка не подтверждена. Исходники Amethyst клонируются из публичного репозитория AngelAuraMC/Amethyst-Android во время сборки. Это неофициальная фанатская сборка; соблюдайте лицензии проекта и компонентов. Debug APK может не устанавливаться поверх официального Amethyst из-за подписи. Не удаляйте старый лаунчер, пока не сохраните важные данные. На устройстве с 2 ГБ ОЗУ Minecraft Java может работать нестабильно.
