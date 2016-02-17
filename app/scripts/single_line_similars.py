#encoding:utf-8
import graphlab as gl
import graphlab.aggregate as agg


data = gl.SFrame.read_csv('/Users/tutu/personal/git/data/non_zero_comparison_nocount.csv', delimiter=',', column_type_hints=[str, str, float])
grouped = data.groupby(
    key_columns='author',
    operations={'similars': agg.CONCAT('similar', 'score')}
)
grouped.save('/Users/tutu/personal/git/data/non_zero_comparison_nocount_oneline.csv', format='csv')
