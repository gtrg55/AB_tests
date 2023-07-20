import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.stats.api as sms
z_score, p_value = sm.stats.proportions_ztest([19398, 19046], [20775, 20853])
print(z_score)
print(p_value)