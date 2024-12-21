# Copyright Aden Handasyde 2019
from django.conf.urls import include
from django.urls import re_path as url
from . import views
from . import models
from django.contrib import admin
from django.urls import path

# ^^^^ Use for cleaning up dodgy datatables

from rest_framework import routers
# ^^^^ Use for cleaning up dodgy datatables

# Each has a sort
# Needs a page-number
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
app_name='Bable'
# path('admin/', admin.site.urls),
router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet)
#router.register(r'post', views.PostViewSet)
	
# Each has a sort
# Needs a page-number
urlpatterns = [
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('i18n/', include('django.conf.urls.i18n')),
	path('examples/', views.ListCreateExampleAPIView.as_view()),
	path('posts/', views.ListCreatePostAPIView.as_view()),
	path('words/', views.ListCreateWordAPIView.as_view()),
	path('sponsor/', views.ListCreateSponsorAPIView.as_view()),
	path('angel_numbers/', views.ListCreateAngelNumberAPIView.as_view()),
	path('angel_number/<number>/', views.ShowAngelNumber, name="show_angel_number"),
	path('angel_numbered/<numbers>/', views.barcode_ai, name="barcode_ai"),
	#path('author/retrieve_by_username/<username>\w+)', views.getByUsername, name='author_username'),
	#path('docs/', include_docs_urls(title='Todo Api')),
	#path('api/v1/todo/', include("todo.urls")),

	#path('stream/', views.stream, name='stream'),
	#path('stream_unseen/', views.stream_unseen, name='stream_unseen'),
	path('api/token', obtain_auth_token, name="auth_token"),
	path('api/jwt/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('checkout/<int:pk>', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
	path('keyup/<int:pk>/<int:post_id>', views.KeyupCheckoutSessionView.as_view(), name='keyup-checkout-session'),

	# path('admin/', admin.site.urls),
	path('logout/', views.logout_user, name='logout_user'),
	path('sign_wallet/', views.sign_wallet, name='sign_wallet'),
	path('autocomplete_votestyles/', views.autocomplete_votestyles, name='autocomplete_votestyles'),
	path('grabvoteid/', views.grabvoteid, name='grabvoteid'),
	#path('gensim_test/', views.gensim_test, name='gensim_test'),
	path('create_product_w_price/<post_id>/', views.create_product_w_price, name='create_product_w_price'),
	path('login/', views.login_view, name='login_view'),
	path('owner/', views.owner, name='owner'),
	path('feedback/', views.feedback, name='feedback'),
	path('create_feedback/', views.create_feedback, name='create_feedback'),
	path('thanks/', views.thanks, name='thanks'),
	path('about/', views.about, name='about'),
	path('management/', views.management, name='management'),
	path('register/', views.register_view, name='register_view'),
	path('dues/', views.tower_of_bable, name='tower_of_bable'),
	path('buy_credits/coinbase/', views.home_view, name='home_view'),
	path('landingpage/', views.landingpage, name='landingpage'),
	path('landingpage/editors_choice/', views.landingpage_editors_choice, name='landingpage_editors_choice'),
	path('landingpage/features_list/', views.landingpage_features_list, name='landingpage_features_list'),
	path('landingpage/goals/', views.landingpage_goals, name='landingpage_goals'),
	path('landingpage/how_tos/', views.landingpage_how_tos, name='landingpage_how_tos'),
	path('landingpage/improvement_notes/', views.landingpage_improvement_notes, name='landingpage_improvement_notes'),
	path('landingpage/mission/', views.landingpage_mission, name='landingpage_mission'),
	path('landingpage/pitch_decks/', views.landingpage_pitch_decks, name='landingpage_pitch_decks'),
	path('landingpage/problems_solutions/', views.landingpage_problems_solutions, name='landingpage_problems_solutions'),
	path('landingpage/roadmaps/', views.landingpage_roadmaps, name='landingpage_roadmaps'),
	path('landingpage/tasks/', views.landingpage_tasks, name='landingpage_tasks'),
	path('landingpage/values/', views.landingpage_values, name='landingpage_values'),
	path('landingpage/vision/', views.landingpage_vision, name='landingpage_vision'),
	path('change_password/', views.change_password, name='change_password'),
	path('search/count/<count>/', views.search, name='search'),
	path('annotate_url/<search_url_id>/', views.annotate_url, name='annotate_url'),
	path('annotate_url_delete/<search_url_id>/', views.delete_annotation_url, name='delete_annotation_url'),
	path('annotate_url_post_comment/<search_url_id>/', views.annotate_url_post_comment, name='annotate_url_post_comment'),
	path('annotate_url_post_comment_location/<search_url_id>/<location_id>/', views.annotate_url_post_comment_location, name='annotate_url_post_comment_location'),
	path('annotate_url_comment_delete/<search_url_id>/<comment_id>/', views.annotate_url_comment_delete, name='annotate_url_comment_delete'),
	path('annotate_url_post_edits/<search_url_id>/', views.annotate_url_post_edits, name='annotate_url_post_edits'),
	path('index/count/<count>/', views.tower_of_bable_count, name='tower_of_bable_count'),
	path('index/time/', views.tower_time, name='tower_time'),
	path('spaces/', views.tob_view_spaces, name='tob_view_spaces'),
	path('spaces/count/<count>/', views.tob_view_spaces_count, name='tob_view_spaces_count'),
	path('space/<space>/count/<count>/', views.tob_space_view_count, name='tob_space_view_count'),
	path('space/<space>/', views.tob_space_view, name='tob_space_view'),
	path('space/<space_id>/post/<post_id>/count/<count>/', views.tob_spaces_post, name='tob_spaces_post'),
	path('space/<space_id>/post/<post_id>/comment/<comment_id>/', views.tob_spaces_posts_comment, name='tob_spaces_posts_comment'),
	path('users/', views.tob_view_users, name='tob_view_users'),
	path('users/count/<count>/', views.tob_view_users_count, name='tob_view_users_count'),
	path('change_dictionary/sort/<sort>/', views.change_dictionary_sort, name='change_dictionary_sort'),
	path('change_attribute/sort/<sort>/', views.change_attribute_sort, name='change_attribute_sort'),
	path('change_anon/sort/<sort>/', views.change_anon_sort, name='change_anon_sort'),
	path('change_anon_sort_char/', views.change_anon_sort_char, name='change_anon_sort_char'),
	path('change_space_sort_char/', views.change_space_sort_char, name='change_space_sort_char'),
	path('change_sponsor_sort_char/', views.change_sponsor_sort_char, name='change_sponsor_sort_char'),
	path('change_dic_sort_char/', views.change_dic_sort_char, name='change_dic_sort_char'),
	path('change_word_sort_char/', views.change_word_sort_char, name='change_word_sort_char'),
	path('change_attribute_sort_char/', views.change_attribute_sort_char, name='change_attribute_sort_char'),
	path('change_comment/sort/<sort>/', views.change_comment_sort, name='change_comment_sort'),
	path('change_word/sort/<sort>/', views.change_word_sort, name='change_word_sort'),
	path('change_post/sort/<sort>/', views.change_post_sort, name='change_post_sort'),
	path('change_post_sort_char/', views.change_post_sort_char, name='change_post_sort_char'),
	path('change_post_filter_from_date/', views.change_post_filter_from_date, name='change_post_filter_from_date'),
	path('change_post_filter_depth/', views.change_post_filter_depth, name='change_post_filter_depth'),
	path('change_storefront_sort_char/', views.change_storefront_sort_char, name='change_storefront_sort_char'),
	path('change_example/sort/<sort>/', views.change_example_sort, name='change_example_sort'),
	path('user/<user>/', views.tob_user_view, name='tob_user_view'),
	path('user/<user>/count/<count>/', views.tob_user_view_count, name='tob_user_view_count'),
	path('user/<user>/storefronts/count/<count>/', views.users_storefronts, name='users_storefronts'),
	path('create_storefront/<dictionary>/', views.create_storefront, name='create_storefront'),
	path('clickthrough_tally/', views.clickthrough_tally, name='clickthrough_tally'),
	path('user/<user>/spaces/count/<count>/', views.tob_users_spaces, name='tob_users_spaces'),
	path('user/<user>/sponsor/<sponsor>/', views.tob_users_sponsor, name='tob_users_sponsor'),
	path('user/<user>/sponsors/count/<count>/', views.tob_users_sponsors, name='tob_users_sponsors'),
	path('user/<user>/space/<space_id>/count/<count>/', views.tob_users_space, name='tob_users_space'),
	path('user/<user>/space/<space_id>/sponsor/<sponsor>/', views.tob_users_spaces_sponsor, name='tob_users_spaces_sponsor'),
	path('user/<user>/space/<space_id>/post/<post_id>/count/<count>/', views.tob_users_spaces_post, name='tob_users_spaces_post'),
	path('user/<user>/vote/<vote>/', views.tob_users_vote, name='tob_users_vote'),
	path('user/<user>/votes/count/<count>/', views.tob_users_votes, name='tob_users_votes'),
	path('user/<user>/space/<space>/post/<post>/count/<count>/', views.tob_users_spaces_post_count, name='tob_users_spaces_post_count'),
	path('user/<user>/space/<space>/post/<post>/comment/<comment>/', views.tob_users_spaces_post_comment, name='tob_users_spaces_post_comment'),
	path('user/<user>/posts/count/<count>/', views.tob_users_posts, name='tob_users_posts'),
	path('user/<user>/post/<post>/count/<count>/', views.tob_users_post, name='tob_users_post'),
	path('user/<user>/post/<post>/comment/<comment>/', views.tob_users_posts_comment, name='tob_users_posts_comment'),
	path('user/<user>/examples/count/<count>/', views.tob_users_examples, name='tob_users_examples'),
	path('user/<user>/dictionaries/count/<count>/', views.tob_users_dics, name='tob_users_dics'),
	path('user/<user>/dictionary/<dictionary>/count/<count>/', views.tob_users_dic, name='tob_users_dic'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/count/<count>/', views.tob_users_dic_word_count, name='tob_users_dic_word_count'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/pronunciation/<pronunciation_id>/', views.tob_users_dic_word_pronunciations, name='tob_users_dic_word_pronunciations'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/attribute/<attribute>/', views.tob_users_dic_word_attribute, name='tob_users_dic_word_attribute'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/similarity/<similarity>/', views.tob_users_dic_word_similarity, name='tob_users_dic_word_similarity'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/translation/<translation>/', views.tob_users_dic_word_translation, name='tob_users_dic_word_translation'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/example/<example>/', views.tob_users_dic_word_example, name='tob_users_dic_word_example'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/story/<story>/', views.tob_users_dic_word_story, name='tob_users_dic_word_story'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/relation/<relation>/', views.tob_users_dic_word_relation, name='tob_users_dic_word_relation'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/sponsor/<sponsor>/', views.tob_users_dic_word_sponsor, name='tob_users_dic_word_sponsor'),
	path('user/<user>/dictionary/<dictionary>/word/<word>/space/<space>/', views.tob_users_dic_word_space, name='tob_users_dic_word_space'),
	path('user/<user>/dictionary/<dictionary>/words/count/<count>/', views.tob_users_dic_words, name='tob_users_dic_words'),
	path('user/<user>/dictionary/<dictionary>/wordgroups/count/<count>/', views.tob_users_dic_wordgroups, name='tob_users_dic_wordgroups'),
	path('user/<user>/dictionary/<dictionary>/translations/count/<count>/', views.tob_users_dic_translations, name='tob_users_dic_translations'),
	path('user/<user>/dictionary/<dictionary>/sentences/count/<count>/', views.tob_users_dic_sentences, name='tob_users_dic_sentences'),
	path('user/<user>/dictionary/<dictionary>/sentences/<sentence>/renditions/count/<count>/', views.tob_users_dic_renditions, name='tob_users_dic_renditions'),
	path('user/<user>/dictionary/<dictionary>/analyses/count/<count>/', views.tob_users_dic_analyses, name='tob_users_dic_analyses'),
	path('user/<user>/dictionary/<dictionary>/votes/count/<count>/', views.tob_users_dic_votes, name='tob_users_dic_votes'),
	path('tob_word/word/<word_id>/', views.tob_word, name='tob_word'),
	path('tob_pronunciations/word/<word_id>/', views.tob_pronunciations, name='tob_pronunciations'),
	path('tob_pronunciation/pron/<pron_id>/', views.tob_pronunciation, name='tob_pronunciation'),
	path('dictionary/', views.tob_dics, name='tob_dics'),
	path('dictionary/<dictionary_id>/', views.tob_dic, name='tob_dic'),
	path('universal_pronunciation/', views.universal_pronunciations, name='universal_pronunciations'),
	path('universal_pronunciation/<pronunciation>/', views.universal_pronunciation, name='universal_pronunciation'),
	path('word_attributes/', views.word_attributess, name='word_attributess'),
	path('word_attributes/<word>/', views.word_attributes, name='word_attributes'),
	path('attribute/<attribute_id>/', views.attribute, name='attribute'),
	path('attributes/<word_id>/', views.attributes, name='attributes'),
	path('mutawords/', views.mutawords, name='mutawords'),
	path('mutaword/<word>/', views.mutaword, name='mutaword'),
	#path('complementary_scholar/', views.complementary_scholar, name='complementary_scholar'),
	path('logout_user/', views.logout_user, name='logout_user'),
	path('create_post/', views.create_post, name='create_post'),
	path('edit_post/<post_id>/', views.edit_post, name='edit_post'),
	path('create_space/', views.create_space, name='create_space'),
	path('create_dic/', views.create_dic, name='create_dic'),
	path('create_task/', views.create_task, name='create_task'),
	path('create_word/', views.create_word, name='create_word'),
	path('create_wordgroup/', views.create_wordgroup, name='create_wordgroup'),
	path('create_translation/', views.create_translation, name='create_translation'),
	path('create_sentence/', views.create_sentence, name='create_sentence'),
	path('create_rendition/', views.create_rendition, name='create_rendition'),
	path('create_analysis/', views.create_analysis, name='create_analysis'),
	path('create_story/', views.create_story, name='create_story'),
	path('create_pronunciations/', views.create_pronunciations, name='create_pronunciations'),
	path('update_own_dic/<dicid>/', views.update_own_dic, name='update_own_dic'),
	path('prereq_own_dic/<dicid>/', views.prereq_own_dic, name='prereq_own_dic'),
	path('want_to_purchase_dic/<dicid>/<invitecode>/', views.want_to_purchase_dic, name='want_to_purchase_dic'),
	path('buy_dic/<dicid>/', views.buy_dic, name='buy_dic'),
	path('submit_buy_dic_form/<dicid>/', views.submit_buy_dic_form, name='submit_buy_dic_form'),
	path('submit_font/<word_id>/', views.submit_font, name='submit_font'),
	path('buy_bread/<amount>/', views.buy_bread, name='buy_bread'),
	path('failed_bread/<amount>/', views.failed_to_purchase_bread, name='failed_to_purchase_bread'),
	path('buy_donate/<amount>/', views.buy_donate, name='buy_donate'),
	path('tob_user_baking/<invoice>/', views.tob_user_baking, name='tob_user_baking'),
	path('apply_votes/', views.apply_votes, name='apply_votes'),
	path('apply_votes_to_votestyle/<voteid>/', views.apply_votes_to_votestyle, name='apply_votes_to_votestyle'),
	path('apply_votestyle/', views.apply_votestyle, name='apply_votestyle'),
	path('exclude_votes/', views.exclude_votes, name='exclude_votes'),
	path('apply_dic/', views.apply_dic, name='apply_dic'),
	path('exclude_dic/', views.exclude_dic, name='exclude_dic'),
	path('create_comment/<source_type>/<source>/<com>/', views.create_comment, name='create_comment'),
	path('create_comment_thread/<source_type>/<source>/<com>/', views.create_comment_thread, name='create_comment_thread'),
	path('buy_users_dic/<user>/<dictionary>/', views.buy_users_dic, name='buy_users_dic'),
	path('delete_own_word/<user>/<dictionary>/<word>/', views.delete_own_word, name='delete_own_word'),
	path('delete_own_word_id/<word_id>/', views.delete_own_word_id, name='delete_own_word_id'),
	path('delete_own_dic/<user>/<dictionary>/', views.delete_own_dic, name='delete_own_dic'),
	path('delete_bought_dic/<user>/<dictionary>/', views.delete_bought_dic, name='delete_bought_dic'),
	path('delete_own_com/<com>/<which>/', views.delete_own_com, name='delete_own_com'),
	path('delete_own_attr/<user>/<dic>/<word>/<attr>/', views.delete_own_attr, name='delete_own_attr'),
	path('delete_own_attr_def/<user>/<dic>/<word>/<attr>/<def>/', views.delete_own_attr_def, name='delete_own_attr_def'),
	path('delete_own_attr_syn/<user>/<dic>/<word>/<attr>/<syn>/', views.delete_own_attr_syn, name='delete_own_attr_syn'),
	path('delete_own_attr_ant/<user>/<dic>/<word>/<attr>/<ant>/', views.delete_own_attr_ant, name='delete_own_attr_ant'),
	path('delete_own_attr_hom/<user>/<dic>/<word>/<attr>/<hom>/', views.delete_own_attr_hom, name='delete_own_attr_hom'),
	path('delete_own_pron/<user>/<dic>/<word>/<pron>/', views.delete_own_pron, name='delete_own_pron'),
	path('delete_own_exam/<user>/<dic>/<word>/<exam>/', views.delete_own_exam, name='delete_own_exam'),
	path('delete_own_trans/<user>/<dic>/<word>/<trans>/', views.delete_own_trans, name='delete_own_trans'),
	path('delete_own_stor/<user>/<dic>/<word>/<stor>/', views.delete_own_stor, name='delete_own_stor'),
	path('delete_own_rela/<user>/<dic>/<word>/<rela>/', views.delete_own_rela, name='delete_own_rela'),
	path('delete_own_conn/<user>/<dic>/<word>/<rela>/<conn>/', views.delete_own_conn, name='delete_own_conn'),
	path('delete_own_spon/<user>/<dic>/<word>/<spon>/', views.delete_own_spon, name='delete_own_spon'),
	path('delete_own_spons/<spon>/', views.delete_own_spons, name='delete_own_spons'),
	path('delete_own_spac/<user>/<dic>/<word>/<spac>/', views.delete_own_spac, name='delete_own_spac'),
	path('delete_own_post/<user>/<post>/', views.delete_own_post, name='delete_own_post'),
	path('delete_own_space/<user>/<space>/', views.delete_own_space, name='delete_own_space'),
	path('delete_own_votestyle/<voteid>/', views.delete_own_votestyle, name='delete_own_votestyle'),
	path('vote/<vote>/', views.vote, name='vote'),
	path('votewvotestyle/<source_type>/<source_id>/', views.votewvotestyle, name='votewvotestyle'),
	path('clickthrough/', views.clickthrough, name='clickthrough'),
	path('viewsponsor/<sponsor_id>/', views.viewsponsor, name='viewsponsor'),
	path('tob_buy_space/<user>/<space>/', views.tob_buy_space, name='tob_buy_space'),
	path('submit_buy_space_form/<space_id>/', views.submit_buy_space_form, name='submit_buy_space_form'),
	path('tob_remove_space/<user>/<space>/', views.tob_remove_space, name='tob_remove_space'),
	path('tob_save_space/<user>/<space>/', views.tob_save_space, name='tob_save_space'),
	path('tob_unsave_space/<user>/<space>/', views.tob_unsave_space, name='tob_unsave_space'),
	path('tob_save_exa/<user>/<exa>/', views.save_own_exa, name='save_own_exa'),
	path('tob_save_com/<user>/<com>/', views.tob_save_com, name='tob_save_com'),
	path('tob_save_votestyle/<user>/<votestyleid>/', views.tob_save_votestyle, name='tob_save_votestyle'),
	path('users_space_edit/<space>/', views.users_space_edit, name='users_space_edit'),
	path('tob_vote/<vote_id>/', views.tob_vote, name='tob_vote'),
	path('tob_post/<post>/', views.tob_post, name='tob_post'),
	path('update_sponsor/', views.update_sponsor, name='update_sponsor'),
	path('tob_sponsor/<sponsor>/', views.tob_sponsor, name='tob_sponsor'),
	path('tob_sponsors/<count>/', views.tob_sponsors, name='tob_sponsors'),
	path('tob_products/<count>/', views.tob_products, name='tob_products'),
	path('tob_product/<product_id>/', views.tob_product, name='tob_product'),
	path('tob_word_sponsor/word_id/<word_id>/sponsor_id/<sponsor_id>/', views.tob_word_sponsor, name='tob_word_sponsor'),
	path('tob_word_translation/word_id/<word_id>/translation_id/<translation_id>/', views.tob_word_translation, name='tob_word_translation'),
	path('tob_word_attribute/word_id/<word_id>/attribute_id/<attribute_id>/', views.tob_word_attribute, name='tob_word_attribute'),
	path('tob_word_pronunciation/word_id/<word_id>/pronunciation_id/<pronunciation_id>/', views.tob_word_pronunciation, name='tob_word_pronunciation'),
	path('tob_pronunciation/<pronunciation_id>/', views.tob_pronunciation, name='tob_pronunciation'),
	path('tob_word_example/word_id/<word_id>/example_id/<example_id>/', views.tob_word_example, name='tob_word_example'),
	path('tob_word_story/word_id/<word_id>/story_id/<story_id>/', views.tob_word_story, name='tob_word_story'),
	path('tob_word_relation/word_id/<word_id>/relation_id/<relation_id>/', views.tob_word_relation, name='tob_word_relation'),
	path('tob_wallet/<vote_id>/', views.tob_wallet, name='tob_wallet'),
	path('submit_wallet/<amount>/', views.submit_wallet, name='submit_wallet'),
	path('tob_email/<token_id>/<count>/', views.tob_email, name='tob_email'),
	path('submit_email/', views.submit_email, name='submit_email'),
	path('kick_vote_for_member/<space_id>/<username>/', views.kick_vote_for_member, name='kick_vote_for_member'),
	path('vote_for_legislative/<space_id>/<username>/', views.vote_for_legislative, name='vote_for_legislative'),
	path('vote_for_administrative/<space_id>/<username>/', views.vote_for_administrative, name='vote_for_administrative'),
	path('vote_for_executive/<space_id>/<username>/', views.vote_for_executive, name='vote_for_executive'),
	path('vote_for_judiciary/<space_id>/<username>/', views.vote_for_judiciary, name='vote_for_judiciary'),
	path('storefronts/<count>/', views.storefronts, name='storefronts'),
	path('edit_storefront/<storefront_id>/', views.edit_storefront, name='edit_storefront'),
	path('storefront/<author>/<dictionary_id>/<storefront_title>/', views.storefront, name='storefront'),
	path('storefront/<author>/<dictionary_id>/<storefront_title>/landing_page/', views.storefront_landing_page, name='storefront_landing_page'),
	path('storefront/<author>/<dictionary_id>/<storefront_title>/product_list/', views.storefront_product_list, name='storefront_product_list'),
	path('storefront/<author>/<dictionary_id>/<storefront_title>/past_purchases/', views.storefront_past_purchases, name='storefront_past_purchases'),
	path('checkout/<author>/<dictionary_id>/<storefront_title>/', views.checkout, name='checkout'),
	path('roadmap/', views.roadmap, name='roadmap'),
	path('upload_file/', views.upload_file, name='upload_file'),
	path('drawing/<author>/<name>/', views.drawing, name='drawing'),
	path('svg_to_gcode/', views.svg_to_gcode, name='svg_to_gcode'),
	path('skizophrenia/', views.barcode, name='barcode'),
	path('tob_users_files/<user>/', views.tob_users_files, name='tob_users_files'),
    path('api/checkout-session/<price_id>/<post_id>/<storefront_id>/', views.create_checkout_session, name='api_checkout_session'),
	path('u/<user>/', views.u, name='u'),
	path('api/checkout-bread-session/<price>/', views.create_checkout_bread_session, name='api_checkout_bread_session'),
	path('api/checkout_ads/', views.checkout_ads, name='checkout_ads'),
]