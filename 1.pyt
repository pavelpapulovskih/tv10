import scipy.stats as stats
# Данные
football_players = [173, 175, 180, 178, 177, 185, 183, 182]
hockey_players = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifters = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166,
170]
# Проведение однофакторного дисперсионного анализа (ANOVA)
f_statistic, p_value = stats.f_oneway(football_players,
hockey_players, weightlifters)
# Вывод результатов
print(f"F-статистика: {f_statistic:.4f}")
print(f"p-значение: {p_value:.4f}")
# Интерпретация результатов
alpha = 0.05
if p_value < alpha:print("Есть статистически значимые различия в среднем росте междугруппами.")
else:print("Нет статистически значимых различий в среднем росте междугруппами.")