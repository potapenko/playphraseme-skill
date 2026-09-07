# Проверка английских примеров лендинга

Редакторское решение для русского мастера, смысловая ревизия 2.
Проверка выполнена по правилам обновлённого локального скилла Codex.
В ChatGPT скилл в рамках этой проверки не устанавливался.

## Что изменено

| Исходный пример | Результат проверки и решение |
| --- | --- |
| I wouldn't miss it for the world | Подтверждён как `I wouldn't miss it for the world.`; сохранены точные текст и пунктуация записи. |
| I can't make it tonight | Точный вариант не подтверждён; выбран `I won't be able to make it tonight.`. |
| How about tomorrow? | Не подтверждён; предложение другого дня заменено на `Maybe we should do this another time.`. |
| I won't be able to attend / Could we reschedule? | Не подтверждены; рабочий сценарий использует `We're going to have to reschedule.`. Уточнены запрос и объяснение: сообщение о необходимости переноса, а не вопрос. |
| cut me some slack | Не подтверждён; диалог про оттенок и уместность использует `Would you give me a break?`. Объяснение переписано под новое выражение. |
| I'm still learning | Не подтверждён; выбран `I'm still getting used to it.`, а ситуация уточнена до привыкания к новой работе. |
| give me a little more time | API вернул расширенную запись `Just give me a little more time.`. Для спокойного объяснения потребности выбран подтверждённый `I need a little time.`. |
| I told you so | Самостоятельная запись не подтверждена; выбран `I don't want to say I told you so.`. Перевод, оттенок и Clip Search ссылка изменены вместе. |
| I guess / I suppose / I think | В качестве самостоятельных записей не подтверждены. Сохранены как предмет сравнения; добавлены полные подтверждённые выражения ниже. |
| I used to / I'm used to | Это конструкции для объяснения. Добавлены две подтверждённые реплики, показывающие разные значения. |
| pick up | Это фразовый глагол для объяснения. Непроверенный сценарий про привычку заменён двумя подтверждёнными выражениями: ответить на звонок и продолжить с прежнего места. |
| carry * forward | Поисковый шаблон, а не запись Common Phrases. Так и представлен; промпт просит скилл подобрать выражения либо выдать готовую ссылку с пропуском. |

## Точные записи, выбранные для страницы

В каждой строке текст дословно получен в `items[].text` указанного публичного
ответа Suggestions и перенесён в поисковую ссылку без изменений.

| Текст Common Phrase | Запрос, подтвердивший запись |
| --- | --- |
| I wouldn't miss it for the world. | [Suggestions: miss world](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=miss%20world&limit=20) |
| I won't be able to make it tonight. | [Suggestions: make tonight](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=make%20tonight&limit=20) |
| Maybe we should do this another time. | [Suggestions: another time](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=another%20time&limit=20) |
| We're going to have to reschedule. | [Suggestions: reschedule](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=reschedule&limit=20) |
| Would you give me a break? | [Suggestions: give break](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=give%20break&limit=20) |
| I'm still getting used to it. | [Suggestions: used to it](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=used%20to%20it&limit=20) |
| I need a little time. | [Suggestions: little time](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=little%20time&limit=20) |
| I guess you could call it that. | [Suggestions: I guess](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=I%20guess&limit=20) |
| I suppose you could call it that. | [Suggestions: I suppose](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=I%20suppose&limit=20) |
| I think you're right. | [Suggestions: I think](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=I%20think&limit=20) |
| I used to go there. | [Suggestions: I used to](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=I%20used%20to&limit=20) |
| I'm kind of used to it. | [Suggestions: used to it](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=used%20to%20it&limit=20) |
| Pick up the phone right now! | [Suggestions: pick up](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=pick%20up&limit=20) |
| Let's pick up where we left off. | [Suggestions: pick up](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=pick%20up&limit=20) |
| I don't want to say I told you so. | [Suggestions: I told you so](https://www.playphrase.me/api/v1/learning/common-phrases/suggestions?language=en&q=I%20told%20you%20so&limit=20) |

Это редакционная карта выбранных примеров, а не сохранённая выгрузка каталога.
Ответы API динамические; ссылка показывает запрос и может вернуть обновлённый
набор в будущем. Числа результатов, уровни и ранги на лендинг не перенесены.

## Как трактовать результат

Проверялись исходные фразы отдельными ограниченными запросами Suggestions,
затем для неподтверждённых вариантов — ключевые слова либо смысловая
альтернатива. Каждый запрос ограничен 20 результатами и 10 секундами;
пагинации, автоматических повторов, авторизации и приватных API не было.

«Не подтверждён» означает, что точная запись не встретилась в проверенных
ответах. Это не доказательство отсутствия в Common Phrases и тем более в
видеокорпусе. Например, исходный полный запрос первого диалога не вернул
нужную запись, а запрос `miss world` её вернул.

Членство в Common Phrases не доказывает интонацию, говорящего или содержание
конкретного клипа. Русские объяснения — редакционная интерпретация английских
выражений. Диалоги остаются примерами, а не дословными проверенными беседами
ChatGPT. Веб-проверка точных обновлённых ссылок и снимки относятся к последующей
подготовке публикации.

## Промпты

Все сценарии русского мастера теперь содержат копируемые текстовые блоки.
Первичные запросы включают реальное имя вызова `@PlayPhrase.me`; реплики
продолжения явно предназначены для того же разговора. Основное действие —
передать задачу скиллу и получить выражения со ссылками. Конкретные фразы в
ответах подтверждены по таблице выше; произвольные будущие ответы на промпты
не объявляются заранее проверенными.

