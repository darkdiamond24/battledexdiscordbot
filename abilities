
import discord
import json
from discord.ext import commands
import pandas as pd
import random
import cv2
import numpy as np
import aiohttp
import re
import battledex

class Ability:
    def __init__(self, name, description, power):
        self.name = name if name else "Unknown"
        self.description = description if description else "No description available."
        self.power = power if power else 0

    def apply(self, target, user=None):
        if self.name == "Rule the Waves":
            return self.rule_the_waves(target)
        elif self.name == "Anschluss":
            return self.anschluss(target)
        elif self.name == "Save the Tsar":
            return self.save_the_tsar(target)
        elif self.name == "Greatest Conqueror":
            return self.greatest_conqueror(target)
        elif self.name == "Ragnarok":
            return self.ragnarok(target)
        elif self.name == "Pax Romana":
            return self.pax_romana(target)
        elif self.name == "Power of an Angel":
            return self.power_of_an_angel(target, user)
        elif self.name == "The Winged Hussars have Arrived":
            return self.winged_hussars(target)
        elif self.name == "The Great Wall of China":
            return self.great_wall_of_china(target)
        elif self.name == "Glory to Kaiser!":
            return self.glory_to_kaiser(target)
        elif self.name == "Too Many States!":
            return self.too_many_states(target)
        elif self.name == "Where am I? I can't see!":
            return self.where_am_i(target)
        elif self.name == "Attila":
            return self.attila(target)
        elif self.name == "Pacific Domination!":
            return self.pacific_domination(target)
        elif self.name == "Fight until the Death!":
            return self.fight_until_the_death(target)
        elif self.name == "Long Live our Soviet Motherland!":
            return self.long_live_soviet_motherland(target)
        elif self.name == "Isolationist Society":
            return self.isolationist_society(target)
        elif self.name == "Home of the Free":
            return self.home_of_the_free(target)
        elif self.name == "Crucifixion":
            return self.crucifixion(target)
        elif self.name == "Lone Star Luck":
            return self.lone_star_luck(target)
        elif self.name == "Never Try to Invade ME":
            return self.never_try_to_invade_me(target)
        elif self.name == "The Silk Roads":
            return self.silk_roads(target)
        elif self.name == "Was Hast Du Gesagt?":
            return self.was_hast_du_gesagt(target)
        elif self.name == "Development, Peace, Prosperity":
            return self.development_peace_prosperity(target)
        elif self.name == "Another Day at Bollywood":
            return self.another_day_at_bollywood(target)
        elif self.name == "Wooden Horse":
            return self.wooden_horse(target)
        elif self.name == "Omae Wa Mou Shindeiru":
            return self.omae_wa_mou_shindeiru(target)
        elif self.name == "United. At Last.":
            return self.united_at_last(target)
        elif self.name == "Hon Hon Hon!":
            return self.hon_hon_hon(target)
        elif self.name == "The Absolute Menace for Europeans":
            return self.absolute_menace_for_europeans(target)
        elif self.name == "Separation":
            return self.separation(target)
        elif self.name == "Streets? We Have Canals":
            return self.streets_we_have_canals(target)
        elif self.name == "Red Light, Green Light":
            return self.red_light_green_light(target)
        elif self.name == "White Flag":
            return self.white_flag(target)
        elif self.name == "World Conquest!":
            return self.world_conquest(target)
        elif self.name == "The Union":
            return self.the_union(target)
        elif self.name == "Remove Greek!":
            return self.remove_greek(target)
        elif self.name == "We Are NOT Greek.":
            return self.we_are_not_greek(target)
        elif self.name == "Long Live the King":
            return self.long_live_the_king(target)
        elif self.name == "Freedom amongst Continental Chaos":
            return self.freedom_amongst_continental_chaos(target)
        elif self.name == "Goat Simulator":
            return self.goat_simulator(target)
        elif self.name == "Mummified!":
            return self.mummified(target)
        elif self.name == "You're Going to Brazil":
            return self.you_are_going_to_brazil(target)
        elif self.name == "It's Called Constantinople!":
            return self.its_called_constantinople(target)
        elif self.name == "I'M NOT DANISH CLAY":
            return self.im_not_danish_clay(target)
        elif self.name == "Africa Is MINE!":
            return self.africa_is_mine(target)
        elif self.name == "Noodles Empire":
            return self.noodles_empire(target)
        elif self.name == "REMOVE TEA!":
            return self.remove_tea(target)
        elif self.name == "Elephant!":
            return self.elephant(target)
        elif self.name == "Mama MIA! Which PIZZA to Choose?":
            return self.mama_mia_which_pizza_to_choose(target)
        elif self.name == "Camicie Nere":
            return self.camicie_nere(target)
        elif self.name == "Parisian Prominence":
            return self.parisian_prominence(target)
        elif self.name == "The Great Pharaoh":
            return self.the_great_pharaoh(target)
        elif self.name == "Workers of the World, Unite!":
            return self.workers_of_the_world_unite(target)
        elif self.name == "Kebab Master":
            return self.kebab_master(target)
        elif self.name == "Colonies Everywhere!":
            return self.colonies_everywhere(target)
        elif self.name == "Only God Is Light":
            return self.only_god_is_light(target)
        elif self.name == "Hellenic Situations":
            return self.hellenic_situations(target)
        elif self.name == "As-Siam Alaikum!":
            return self.as_siam_alaikum(target)
        elif self.name == "Unification":
            return self.unification(target)
        elif self.name == "So Big!":
            return self.so_big(target)
        elif self.name == "United for Allah":
            return self.united_for_allah(target)
        elif self.name == "Secession War":
            return self.secession_war(target)
        elif self.name == "Par Toutatis!":
            return self.par_toutatis(target)
        elif self.name == "Father of Europe":
            return self.father_of_europe(target)
        elif self.name == "No Worries, I Can Swim":
            return self.no_worries_i_can_swim(target)
        elif self.name == "Treaty of Trianon":
            return self.treaty_of_trianon(target)
        elif self.name == "2012":
            return self.twenty_twelve(target)
        elif self.name == "Too Many Minorities!":
            return self.too_many_minorities(target)
        elif self.name == "Work, Only Work":
            return self.work_only_work(target)
        elif self.name == "The Life: Survival Edition":
            return self.the_life_survival_edition(target)
        elif self.name == "Power of Friendship and Money":
            return self.power_of_friendship_and_money(target)
        elif self.name == "Shalom!":
            return self.shalom(target)
        elif self.name == "CHARGE!":
            return self.charge(target)
        elif self.name == "Without the S":
            return self.without_the_s(target)
        elif self.name == "Remember the Vasa":
            return self.remember_the_vasa(target)
        elif self.name == "Too Many Colonies":
            return self.too_many_colonies(target)
        elif self.name == "Trading Galore!":
            return self.trading_galore(target)
        elif self.name == "Oil Master":
            return self.oil_master(target)
        elif self.name == "Heil Charlemagne!":
            return self.heil_charlemagne(target)
        elif self.name == "I Am Useful I Swear…":
            return self.i_am_useful_i_swear(target)
        elif self.name == "The Bank":
            return self.the_bank(target)
        elif self.name == "Black and White":
            return self.black_and_white(target)
        elif self.name == "European in the Heart":
            return self.european_in_the_heart(target)
        elif self.name == "I'm Sorry":
            return self.im_sorry(target)
        elif self.name == "Mafia Mayhem":
            return self.mafia_mayhem(target)
        elif self.name == "Forever Comrades":
            return self.forever_comrades(target)
        elif self.name == "Cannot Go to Space":
            return self.cannot_go_to_space(target)
        elif self.name == "Project I.K.E.A.":
            return self.project_ikea(target)
        elif self.name == "Raise the Stakes":
            return self.raise_the_stakes(target)
        elif self.name == "SCOTLAND FOREVER!":
            return self.scotland_forever(target)
        elif self.name == "Elon Musk":
            return self.elon_musk(target)
        elif self.name == "There Are No Debts":
            return self.there_are_no_debts(target)
        elif self.name == "No More Capitalism":
            return self.no_more_capitalism(target)
        elif self.name == "We Love Gunpowder!":
            return self.we_love_gunpowder(target)
        elif self.name == "Long Live Thailand":
            return self.long_live_thailand(target)
        elif self.name == "Armenis Is OURS!":
            return self.armenis_is_ours(target)
        elif self.name == "Strongest Army?":
            return self.strongest_army(target)
        elif self.name == "Plunder":
            return self.plunder(target)
        elif self.name == "Treaty of Rome":
            return self.treaty_of_rome(target)
        elif self.name == "I Don't Trust You":
            return self.i_dont_trust_you(target)
        elif self.name == "Who Owns Me?":
            return self.who_owns_me(target)
        elif self.name == "Article 5":
            return self.article_5(target)
        elif self.name == "Guernica":
            return self.guernica(target)
        elif self.name == "United Against Our Enemy":
            return self.united_against_our_enemy(target)
        elif self.name == "We All Need Peace":
            return self.we_all_need_peace(target)
        elif self.name == "I Have the Power":
            return self.i_have_the_power(target)
        elif self.name == "No Army, No Money":
            return self.no_army_no_money(target)
        elif self.name == "Rice Cooker":
            return self.rice_cooker(target)
        elif self.name == "Coups, Civil Wars, Chaos":
            return self.coups_civil_wars_chaos(target)
        elif self.name == "Cook's Curse":
            return self.cooks_curse(target)
        elif self.name == "Prehistoric Persistence":
            return self.prehistoric_persistence(target)
        elif self.name == "Symmetry":
            return self.symmetry(target)
        elif self.name == "Child of the Mongols":
            return self.child_of_the_mongols(target)
        elif self.name == "Prost!":
            return self.prost(target)
        elif self.name == "DZ":
            return self.dz(target)
        elif self.name == "Sun Protection":
            return self.sun_protection(target)
        elif self.name == "Cheap Market Place":
            return self.cheap_market_place(target)
        elif self.name == "Pablo Escobar":
            return self.pablo_escobar(target)
        elif self.name == "Beeeeeers…":
            return self.beeeeers(target)
        elif self.name == "Peace Cannot Exist":
            return self.peace_cannot_exist(target)
        elif self.name == "Kebab Version of USA":
            return self.kebab_version_of_usa(target)
        elif self.name == "Dia De Muertos":
            return self.dia_de_muertos(target)
        elif self.name == "Military Junta":
            return self.military_junta(target)
        elif self.name == "Hard Weed":
            return self.hard_weed(target)
        elif self.name == "Republic of Scams":
            return self.republic_of_scams(target)
        elif self.name == "Time Does Not Pass":
            return self.time_does_not_pass(target)
        elif self.name == "Incas Soul":
            return self.incas_soul(target)
        elif self.name == "The Real Chosen Land":
            return self.the_real_chosen_land(target)
        elif self.name == "Nação Valente":
            return self.nacao_valente(target)
        elif self.name == "The War Art":
            return self.the_war_art(target)
        elif self.name == "Vampire Impact":
            return self.vampire_impact(target)
        elif self.name == "The Best Harbor":
            return self.the_best_harbor(target)
        elif self.name == "11/10 Be Neutral":
            return self.eleven_ten_be_neutral(target)
        elif self.name == "Syria Bachar":
            return self.syria_bachar(target)
        elif self.name == "The Power of Twitch":
            return self.the_power_of_twitch(target)
        elif self.name == "Dubai Style":
            return self.dubai_style(target)
        elif self.name == "¡Inflacion!":
            return self.inflacion(target)
        elif self.name == "Drowning in Gold!":
            return self.drowning_in_gold(target)
        elif self.name == "Free Amid the Free":
            return self.free_amid_the_free(target)
        elif self.name == "Disbandment":
            return self.disbandment(target)
        elif self.name == "Philosophy!":
            return self.philosophy(target)
        elif self.name == "This Is SPARTA!":
            return self.this_is_sparta(target)
        elif self.name == "The First Kingdom":
            return self.the_first_kingdom(target)
        elif self.name == "Woosh!":
            return self.woosh(target)
        elif self.name == "Last Free African Country…":
            return self.last_free_african_country(target)
        elif self.name == "Bob Morane":
            return self.bob_morane(target)
        elif self.name == "Tidal Wave":
            return self.tidal_wave(target)
        elif self.name == "Backstab":
            return self.backstab(target)
        elif self.name == "Vive le Quebec!":
            return self.vive_le_quebec(target)
        elif self.name == "Maha Siam Happy!":
            return self.maha_siam_happy(target)
        elif self.name == "Full Metal Jacket":
            return self.full_metal_jacket(target)
        elif self.name == "I Am the Real China":
            return self.i_am_the_real_china(target)
        elif self.name == "Land of the Sheep":
            return self.land_of_the_sheep(target)
        elif self.name == "Let's Rebuild Europe!":
            return self.lets_rebuild_europe(target)
        elif self.name == "Suez Is MINE!":
            return self.suez_is_mine(target)
        elif self.name == "Art Like Gold":
            return self.art_like_gold(target)
        elif self.name == "Glory to Builders":
            return self.glory_to_builders(target)
        elif self.name == "No Kangaroos in Austria!":
            return self.no_kangaroos_in_austria(target)
        elif self.name == "I Have One Enemy":
            return self.i_have_one_enemy(target)
        elif self.name == "Columbus":
            return self.columbus(target)
        elif self.name == "Where is USSR?":
            return self.where_is_ussr(target)
        elif self.name == "The Best Shortcut":
            return self.the_best_shortcut(target)
        elif self.name == "Give Me Sea":
            return self.give_me_sea(target)
        elif self.name == "Stronk!":
            return self.stronk(target)
        elif self.name == "It's a Worm?":
            return self.its_a_worm(target)
        elif self.name == "Don't Talk About the Past":
            return self.dont_talk_about_the_past(target)
        elif self.name == "Embargo Boy":
            return self.embargo_boy(target)
        elif self.name == "The Best Island Nation!":
            return self.the_best_island_nation(target)
        elif self.name == "Don't Walk on the Lego":
            return self.dont_walk_on_the_lego(target)
        elif self.name == "Doctor Ball":
            return self.doctor_ball(target)
        elif self.name == "Around the Equator":
            return self.around_the_equator(target)
        elif self.name == "Please Foods and Moneys":
            return self.please_foods_and_moneys(target)
        elif self.name == "Just Happy!":
            return self.just_happy(target)
        elif self.name == "Hungryball":
            return self.hungryball(target)
        elif self.name == "¡Fuego en El Agujero!":
            return self.fuego_en_el_agujero(target)
        elif self.name == "Smokin' that Pack":
            return self.smokin_that_pack(target)
        elif self.name == "Stop Calling Me Micheal Jordan.":
            return self.stop_calling_me_micheal_jordan(target)
        elif self.name == "You Want To Go Into Space?":
            return self.you_want_to_go_into_space(target)
        elif self.name == "The True Warrior":
            return self.the_true_warrior(target)
        elif self.name == "Too Lazy":
            return self.too_lazy(target)
        elif self.name == "Literacy and Corruption":
            return self.literacy_and_corruption(target)
        elif self.name == "Haram":
            return self.haram(target)
        elif self.name == "I Am a Tree":
            return self.i_am_a_tree(target)
        elif self.name == "You Want Oil?":
            return self.you_want_oil(target)
        elif self.name == "Slavery Mood":
            return self.slavery_mood(target)
        elif self.name == "Fortitude of Europe":
            return self.fortitude_of_europe(target)
        elif self.name == "Kebab Removing Agency":
            return self.kebab_removing_agency(target)
        elif self.name == "Without Caution, Wisdom is Useless…":
            return self.without_caution_wisdom_is_useless(target)
        elif self.name == "Sri Jayawardenepura Kotte":
            return self.sri_jayawardenepura_kotte(target)
        elif self.name == "You're the Victim of Your Own Mistakes.":
            return self.you_are_the_victim_of_your_own_mistakes(target)
        elif self.name == "Isn't Tatooine":
            return self.isnt_tatooine(target)
        elif self.name == "Don't Care about the Pandemic":
            return self.dont_care_about_the_pandemic(target)
        elif self.name == "Neutral in America":
            return self.neutral_in_america(target)
        elif self.name == "Double Landlocked":
            return self.double_landlocked(target)
        elif self.name == "Yeah Man (Sad and Poor)":
            return self.yeah_man_sad_and_poor(target)
        elif self.name == "Syrupy Succulence":
            return self.syrupy_succulence(target)
        elif self.name == "The Home of the Sheep":
            return self.the_home_of_the_sheep(target)
        elif self.name == "Power of Chilli":
            return self.power_of_chilli(target)
        elif self.name == "Diamonds! Diamonds! Diamonds!":
            return self.diamonds_diamonds_diamonds(target)
        elif self.name == "We Need to Build a Wall!":
            return self.we_need_to_build_a_wall(target)
        elif self.name == "Terrortorial Expanasion":
            return self.terrortorial_expanasion(target)
        elif self.name == "18 June 1940":
            return self.eighteen_june_1940(target)
        elif self.name == "Embrace Our Power!":
            return self.embrace_our_power(target)
        elif self.name == "We Are Sinking!!":
            return self.we_are_sinking(target)
        elif self.name == "Shipbuilders":
            return self.shipbuilders(target)
        elif self.name == "Meditation":
            return self.meditation(target)
        elif self.name == "In Coop We Trust":
            return self.in_coop_we_trust(target)
        elif self.name == "Slippy Slopes":
            return self.slippy_slopes(target)
        elif self.name == "The Power of the Shell":
            return self.the_power_of_the_shell(target)
        elif self.name == "Unify Italy!":
            return self.unify_italy(target)
        elif self.name == "Ruler of Egypt":
            return self.ruler_of_egypt(target)
        elif self.name == "Radiation Detected":
            return self.radiation_detected(target)
        elif self.name == "Three Eyes":
            return self.three_eyes(target)
        elif self.name == "Tonga Time":
            return self.tonga_time(target)
        elif self.name == "Angkor Wat":
            return self.angkor_wat(target)
        elif self.name == "Broken Trident":
            return self.broken_trident(target)
        elif self.name == "Holy Ambitions":
            return self.holy_ambitions(target)
        elif self.name == "Vast Atolls":
            return self.vast_atolls(target)
        elif self.name == "Kebab Protection":
            return self.kebab_protection(target)
        elif self.name == "Brainball":
            return self.brainball(target)
        elif self.name == "Tourists' Money is Mine":
            return self.tourists_money_is_mine(target)
        elif self.name == "Gigachad":
            return self.gigachad(target)
        elif self.name == "Not Free Yet…":
            return self.not_free_yet(target)
        elif self.name == "Brutal Dictatorship":
            return self.brutal_dictatorship(target)
        elif self.name == "Screw Crusaders!":
            return self.screw_crusaders(target)
        elif self.name == "It's Scratching Me…":
            return self.its_scratching_me(target)
        elif self.name == "Coffin Dance":
            return self.coffin_dance(target)
        elif self.name == "The Eternal Spring":
            return self.the_eternal_spring(target)
        elif self.name == "The Power of Oil":
            return self.the_power_of_oil(target)
        elif self.name == "Saint Partick's Day":
            return self.saint_particks_day(target)
        elif self.name == "XBOX Ball":
            return self.xbox_ball(target)
        elif self.name == "Potato Farmer":
            return self.potato_farmer(target)
        elif self.name == "Try Again!":
            return self.try_again(target)
        elif self.name == "Terrorism Everywhere":
            return self.terrorism_everywhere(target)
        elif self.name == "The Order of Malta":
            return self.the_order_of_malta(target)
        elif self.name == "Underpopulated":
            return self.underpopulated(target)
        elif self.name == "Save My Kiwis":
            return self.save_my_kiwis(target)
        elif self.name == "Colonized":
            return self.colonized(target)
        elif self.name == "Baby Slavic":
            return self.baby_slavic(target)
        elif self.name == "Voodoo Masters.":
            return self.voodoo_masters(target)
        elif self.name == "I Don't Like Politics":
            return self.i_dont_like_politics(target)
        elif self.name == "Mine Copper":
            return self.mine_copper(target)
        elif self.name == "Angry and Rich":
            return self.angry_and_rich(target)
        elif self.name == "London Liberation":
            return self.london_liberation(target)
        elif self.name == "The National Dance":
            return self.the_national_dance(target)
        elif self.name == "500 Years Stronk!":
            return self.five_hundred_years_stronk(target)
        elif self.name == "Succession":
            return self.succession(target)
        elif self.name == "No Army":
            return self.no_army(target)
        elif self.name == "Year of Rivers":
            return self.year_of_rivers(target)
        elif self.name == "The Taste of Cashew":
            return self.the_taste_of_cashew(target)
        elif self.name == "African Democracy":
            return self.african_democracy(target)
        elif self.name == "Postage Stamps":
            return self.postage_stamps(target)
        elif self.name == "Fair Trade":
            return self.fair_trade(target)
        elif self.name == "Rainbow Attack":
            return self.rainbow_attack(target)
        elif self.name == "This Is the Home of the Brave":
            return self.this_is_the_home_of_the_brave(target)
        elif self.name == "Red and Black, I Dress Eagle":
            return self.red_and_black_i_dress_eagle(target)
        elif self.name == "The Great Blue Hole":
            return self.the_great_blue_hole(target)
        elif self.name == "A Lot of Memories":
            return self.a_lot_of_memories(target)
        elif self.name == "Beep Boop":
            return self.beep_boop(target)
        elif self.name == "Civil War!":
            return self.civil_war(target)
        elif self.name == "Tea Farm":
            return self.tea_farm(target)
        elif self.name == "I'm the Real Congo":
            return self.im_the_real_congo(target)
        elif self.name == "I Don't Like My Violent Brother!":
            return self.i_dont_like_my_violent_brother(target)
        elif self.name == "Kill is an Art":
            return self.kill_is_an_art(target)
        elif self.name == "Can I Into Nordic?":
            return self.can_i_into_nordic(target)
        elif self.name == "Absolute Decree":
            return self.absolute_decree(target)
        elif self.name == "Island Hopping":
            return self.island_hopping(target)
        elif self.name == "I Don't Want to be German!":
            return self.i_dont_want_to_be_german(target)
        elif self.name == "River Nation":
            return self.river_nation(target)
        elif self.name == "Tourism Industries":
            return self.tourism_industries(target)
        elif self.name == "Banana Republic":
            return self.banana_republic(target)
        elif self.name == "Ne m'appelez pas 'Ivory Coast'":
            return self.ne_mappelez_pas_ivory_coast(target)
        elif self.name == "I Refuse to Join the SSR!":
            return self.i_refuse_to_join_the_ssr(target)
        elif self.name == "Landlocked Communist":
            return self.landlocked_communist(target)
        elif self.name == "Another Explosion":
            return self.another_explosion(target)
        elif self.name == "Europe's Child":
            return self.europes_child(target)
        elif self.name == "Not Vodka Puppet":
            return self.not_vodka_puppet(target)
        elif self.name == "Kingdom Clash":
            return self.kingdom_clash(target)
        elif self.name == "Weapons Lover":
            return self.weapons_lover(target)
        elif self.name == "Rawr!":
            return self.rawr(target)
        elif self.name == "No Imperialism!":
            return self.no_imperialism(target)
        elif self.name == "Fertility Rate":
            return self.fertility_rate(target)
        elif self.name == "Intifada until the End":
            return self.intifada_until_the_end(target)
        elif self.name == "Humiliated…":
            return self.humiliated(target)
        elif self.name == "The Mother Colony":
            return self.the_mother_colony(target)
        elif self.name == "Drive in Volcano":
            return self.drive_in_volcano(target)
        elif self.name == "Pirates VS Pirates":
            return self.pirates_vs_pirates(target)
        elif self.name == "Young and already Sad…":
            return self.young_and_already_sad(target)
        elif self.name == "Very Stable Country":
            return self.very_stable_country(target)
        elif self.name == "Kebab Friends":
            return self.kebab_friends(target)
        elif self.name == "Hakuna Matata!":
            return self.hakuna_matata(target)
        elif self.name == "I AM REAL!":
            return self.i_am_real(target)
        elif self.name == "Dissolution":
            return self.dissolution(target)
        elif self.name == "Green Cape":
            return self.green_cape(target)
        elif self.name == "Diamonds":
            return self.diamonds(target)
        elif self.name == "Isle of Spice":
            return self.isle_of_spice(target)
        elif self.name == "Jellyfish Isle":
            return self.jellyfish_isle(target)
        elif self.name == "Scuba Galore":
            return self.scuba_galore(target)
        elif self.name == "Jewels of the Carribean":
            return self.jewels_of_the_carribean(target)
        elif self.name == "Cannibalism":
            return self.cannibalism(target)
        elif self.name == "Stronk Kebab Remover":
            return self.stronk_kebab_remover(target)
        elif self.name == "Stop Calling Me Qatar!":
            return self.stop_calling_me_qatar(target)
        elif self.name == "365 Beaches":
            return self.three_sixty_five_beaches(target)
        elif self.name == "Venice of Africa":
            return self.venice_of_africa(target)
        elif self.name == "Let the Dragon be Your Way":
            return self.let_the_dragon_be_your_way(target)
        elif self.name == "Hunger Games":
            return self.hunger_games(target)
        elif self.name == "Two Capitals.":
            return self.two_capitals(target)
        elif self.name == "Countryballs Kart Wii":
            return self.countryballs_kart_wii(target)
        elif self.name == "Perfume Isles":
            return self.perfume_isles(target)
        elif self.name == "America's Tom Thumb":
            return self.americas_tom_thumb(target)
        elif self.name == "It's Corruption Time!":
            return self.its_corruption_time(target)
        elif self.name == "Please Make Me Free":
            return self.please_make_me_free(target)
        elif self.name == "Volcano's Awakening":
            return self.volcanos_awakening(target)
        elif self.name == "The Power of Water":
            return self.the_power_of_water(target)
        elif self.name == "I'M NOT SERBIAN CLAY":
            return self.im_not_serbian_clay(target)
        elif self.name == "Liberian Ways of Life":
            return self.liberian_ways_of_life(target)
        elif self.name == "In the Sky":
            return self.in_the_sky(target)
        elif self.name == "More Companies than People":
            return self.more_companies_than_people(target)
        elif self.name == "I Like to Move it Move it":
            return self.i_like_to_move_it_move_it(target)
        elif self.name == "Mhajahit- Majahapit- ?!":
            return self.mhajahit_majahapit(target)
        elif self.name == "Smile for the Picture!":
            return self.smile_for_the_picture(target)
        elif self.name == "Home of the Dodo":
            return self.home_of_the_dodo(target)
        elif self.name == "Sleep on the Top":
            return self.sleep_on_the_top(target)
        elif self.name == "The Floor is Lava":
            return self.the_floor_is_lava(target)
        elif self.name == "Taxes!!":
            return self.taxes(target)
        elif self.name == "Cover me in Sunshine":
            return self.cover_me_in_sunshine(target)
        elif self.name == "Welcom to My Canal":
            return self.welcome_to_my_canal(target)
        elif self.name == "Survivor: Season 5":
            return self.survivor_season_5(target)
        elif self.name == "Vive La Commune!":
            return self.vive_la_commune(target)
        elif self.name == "Cleanliness":
            return self.cleanliness(target)
        elif self.name == "Senegal":
            return self.senegal(target)
        elif self.name == "Come to Ebola Family":
            return self.come_to_ebola_family(target)
        elif self.name == "Pirates!":
            return self.pirates(target)
        elif self.name == "Isn't a Surname":
            return self.isnt_a_surname(target)
        elif self.name == "Portuguese Empire's Last Eastern Hope":
            return self.portuguese_empires_last_eastern_hope(target)
        elif self.name == "Elephant Stampede":
            return self.elephant_stampede(target)
        elif self.name == "Dj Booty":
            return self.dj_booty(target)

    def rule_the_waves(self, target):
        if not hasattr(self, 'rule_the_waves_used'):
            self.rule_the_waves_used = 0
        if self.rule_the_waves_used >= 2:
            return f"{self.name} cannot use Rule the Waves anymore."

        if not hasattr(target, 'blocked_turns'):
            target.blocked_turns = 0
        target.blocked_turns += 1
        self.rule_the_waves_used += 1
        return f"{target.name} is affected by Rule the Waves and is blocked for 1 turn!"

    def anschluss(self, target):
        if not hasattr(target, 'anschluss_used'):
            target.anschluss_used = set()
        available_damages = {i for i in range(100, 1100, 100)} - target.anschluss_used
        if not available_damages:
            return f"{target.name} has no available damage options left for Anschluss."

        chosen_damage = random.choice(list(available_damages))
        target.hp -= chosen_damage
        target.anschluss_used.add(chosen_damage)
        return f"{target.name} is affected by Anschluss and takes {chosen_damage} damage!"

    def save_the_tsar(self, target):
        target.protected_turns = 3
        return f"{target.name} is now protected for the next 3 turns and cannot be attacked!"

    def greatest_conqueror(self, target):
        stolen_hp = target.hp // 2
        stolen_atk = target.atk // 2
        target.hp -= stolen_hp
        target.atk -= stolen_atk
        mongol_empire = next((ball for ball in decks[self.user.id] if ball.name == "Mongol Empire"), None)
        if mongol_empire:
            mongol_empire.hp += stolen_hp
            mongol_empire.atk += stolen_atk
            return f"{target.name} is affected by Greatest Conqueror! {stolen_hp} HP and {stolen_atk} ATK are stolen and added to Mongol Empire!"
        else:
            return f"{target.name} is affected by Greatest Conqueror! But Mongol Empire is not in the deck to receive the stolen stats."

    def ragnarok(self, target):
        kalmar_union = next((ball for ball in decks[self.user.id] if ball.name == "Kalmar Union"), None)
        if kalmar_union:
            if kalmar_union.hp < 150:
                kalmar_union.atk *= 2
            return f"{kalmar_union.name}'s HP dropped below 150! Their ATK is now doubled."
        else:
            kalmar_union.atk /= 2
            return f"{kalmar_union.name}'s HP rose above 300! Their ATK is now back to normal."
        return f"{target.name} is unaffected by Ragnarok!"

    def pax_romana(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Pax Romana!"

    def power_of_an_angel(self, target, user):
        # Implement the ability logic here
        return f"{target.name} is affected by Power of an Angel!"

    def winged_hussars(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Winged Hussars have Arrived!"

    def great_wall_of_china(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Great Wall of China!"

    def glory_to_kaiser(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Glory to Kaiser!"

    def too_many_states(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Too Many States!"

    def where_am_i(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Where am I? I can't see!"

    def attila(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Attila!"

    def pacific_domination(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Pacific Domination!"

    def fight_until_the_death(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Fight until the Death!"

    def long_live_soviet_motherland(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Long Live our Soviet Motherland!"

    def isolationist_society(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Isolationist Society!"

    def home_of_the_free(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Home of the Free!"

    def crucifixion(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Crucifixion!"

    def lone_star_luck(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Lone Star Luck!"

    def never_try_to_invade_me(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Never Try to Invade ME!"

    def silk_roads(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Silk Roads!"

    def was_hast_du_gesagt(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Was Hast Du Gesagt?"

    def development_peace_prosperity(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Development, Peace, Prosperity!"

    def another_day_at_bollywood(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Another Day at Bollywood!"

    def wooden_horse(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Wooden Horse!"

    def omae_wa_mou_shindeiru(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Omae Wa Mou Shindeiru!"

    def united_at_last(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by United. At Last.!"

    def hon_hon_hon(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Hon Hon Hon!"

    def absolute_menace_for_europeans(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Absolute Menace for Europeans!"

    def separation(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Separation!"

    def streets_we_have_canals(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Streets? We Have Canals!"

    def red_light_green_light(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Red Light, Green Light!"

    def white_flag(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by White Flag!"

    def world_conquest(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by World Conquest!"

    def the_union(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Union!"

    def remove_greek(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Remove Greek!"

    def we_are_not_greek(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by We Are NOT Greek."

    def long_live_the_king(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Long Live the King!"

    def freedom_amongst_continental_chaos(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Freedom amongst Continental Chaos!"

    def goat_simulator(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Goat Simulator!"

    def mummified(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Mummified!"

    def you_are_going_to_brazil(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by You're Going to Brazil!"

    def its_called_constantinople(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by It's Called Constantinople!"

    def im_not_danish_clay(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I'M NOT DANISH CLAY!"

    def africa_is_mine(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Africa Is MINE!"

    def noodles_empire(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Noodles Empire!"

    def remove_tea(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by REMOVE TEA!"

    def elephant(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Elephant!"

    def mama_mia_which_pizza_to_choose(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Mama MIA! Which PIZZA to Choose?"

    def camicie_nere(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Camicie Nere!"

    def parisian_prominence(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Parisian Prominence!"

    def the_great_pharaoh(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Great Pharaoh!"

    def workers_of_the_world_unite(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Workers of the World, Unite!"

    def kebab_master(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Kebab Master!"

    def colonies_everywhere(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Colonies Everywhere!"

    def only_god_is_light(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Only God Is Light!"

    def hellenic_situations(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Hellenic Situations!"

    def as_siam_alaikum(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by As-Siam Alaikum!"

    def unification(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Unification!"

    def so_big(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by So Big!"

    def united_for_allah(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by United for Allah!"

    def secession_war(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Secession War!"

    def par_toutatis(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Par Toutatis!"

    def father_of_europe(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Father of Europe!"

    def no_worries_i_can_swim(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by No Worries, I Can Swim!"

    def treaty_of_trianon(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Treaty of Trianon!"

    def twenty_twelve(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by 2012!"

    def too_many_minorities(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Too Many Minorities!"

    def work_only_work(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Work, Only Work!"

    def the_life_survival_edition(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Life: Survival Edition!"

    def power_of_friendship_and_money(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Power of Friendship and Money!"

    def shalom(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Shalom!"

    def charge(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by CHARGE!"

    def without_the_s(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Without the S!"

    def remember_the_vasa(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Remember the Vasa!"

    def too_many_colonies(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Too Many Colonies!"

    def trading_galore(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Trading Galore!"

    def oil_master(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Oil Master!"

    def heil_charlemagne(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Heil Charlemagne!"

    def i_am_useful_i_swear(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Am Useful I Swear…"

    def the_bank(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Bank!"

    def black_and_white(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Black and White!"

    def european_in_the_heart(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by European in the Heart!"

    def im_sorry(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I'm Sorry!"

    def mafia_mayhem(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Mafia Mayhem!"

    def forever_comrades(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Forever Comrades!"

    def cannot_go_to_space(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Cannot Go to Space!"

    def project_ikea(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Project I.K.E.A.!"

    def raise_the_stakes(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Raise the Stakes!"

    def scotland_forever(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by SCOTLAND FOREVER!"

    def elon_musk(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Elon Musk!"

    def there_are_no_debts(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by There Are No Debts!"

    def no_more_capitalism(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by No More Capitalism!"

    def we_love_gunpowder(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by We Love Gunpowder!"

    def long_live_thailand(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Long Live Thailand!"

    def armenis_is_ours(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Armenis Is OURS!"

    def strongest_army(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Strongest Army?"

    def plunder(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Plunder!"

    def treaty_of_rome(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Treaty of Rome!"

    def i_dont_trust_you(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Don't Trust You!"

    def who_owns_me(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Who Owns Me?"

    def article_5(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Article 5!"

    def guernica(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Guernica!"

    def united_against_our_enemy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by United Against Our Enemy!"

    def we_all_need_peace(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by We All Need Peace!"

    def i_have_the_power(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Have the Power!"

    def no_army_no_money(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by No Army, No Money!"

    def rice_cooker(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Rice Cooker!"

    def coups_civil_wars_chaos(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Coups, Civil Wars, Chaos!"

    def cooks_curse(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Cook's Curse!"

    def prehistoric_persistence(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Prehistoric Persistence!"

    def symmetry(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Symmetry!"

    def child_of_the_mongols(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Child of the Mongols!"

    def prost(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Prost!"

    def dz(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by DZ!"

    def sun_protection(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Sun Protection!"

    def cheap_market_place(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Cheap Market Place!"

    def pablo_escobar(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Pablo Escobar!"

    def beeeeeers(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Beeeeeers…"

    def peace_cannot_exist(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Peace Cannot Exist!"

    def kebab_version_of_usa(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Kebab Version of USA!"

    def dia_de_muertos(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Dia De Muertos!"

    def military_junta(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Military Junta!"

    def hard_weed(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Hard Weed!"

    def republic_of_scams(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Republic of Scams!"

    def time_does_not_pass(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Time Does Not Pass!"

    def incas_soul(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Incas Soul!"

    def the_real_chosen_land(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Real Chosen Land!"

    def nacao_valente(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Nação Valente!"

    def the_war_art(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The War Art!"

    def vampire_impact(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Vampire Impact!"

    def the_best_harbor(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Best Harbor!"

    def eleven_ten_be_neutral(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by 11/10 Be Neutral!"

    def syria_bachar(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Syria Bachar!"

    def the_power_of_twitch(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Power of Twitch!"

    def dubai_style(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Dubai Style!"

    def inflacion(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by ¡Inflacion!"

    def drowning_in_gold(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Drowning in Gold!"

    def free_amid_the_free(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Free Amid the Free!"

    def disbandment(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Disbandment!"

    def philosophy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Philosophy!"

    def this_is_sparta(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by This Is SPARTA!"

    def the_first_kingdom(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The First Kingdom!"

    def woosh(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Woosh!"

    def last_free_african_country(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Last Free African Country…"

    def bob_morane(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Bob Morane!"

    def tidal_wave(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Tidal Wave!"

    def backstab(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Backstab!"

    def vive_le_quebec(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Vive le Quebec!"

    def maha_siam_happy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Maha Siam Happy!"

    def full_metal_jacket(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Full Metal Jacket!"

    def i_am_the_real_china(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Am the Real China!"

    def land_of_the_sheep(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Land of the Sheep!"

    def lets_rebuild_europe(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Let's Rebuild Europe!"

    def suez_is_mine(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Suez Is MINE!"

    def art_like_gold(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Art Like Gold!"

    def glory_to_builders(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Glory to Builders!"

    def no_kangaroos_in_austria(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by No Kangaroos in Austria!"

    def i_have_one_enemy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Have One Enemy!"

    def columbus(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Columbus!"

    def where_is_ussr(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Where is USSR?"

    def the_best_shortcut(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Best Shortcut!"

    def give_me_sea(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Give Me Sea!"

    def stronk(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Stronk!"

    def its_a_worm(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by It's a Worm?"

    def dont_talk_about_the_past(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Don't Talk About the Past!"

    def embargo_boy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Embargo Boy!"

    def the_best_island_nation(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Best Island Nation!"

    def dont_walk_on_the_lego(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Don't Walk on the Lego!"

    def doctor_ball(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Doctor Ball!"

    def around_the_equator(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Around the Equator!"

    def please_foods_and_moneys(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Please Foods and Moneys!"

    def just_happy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Just Happy!"

    def hungryball(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Hungryball!"

    def fuego_en_el_agujero(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by ¡Fuego en El Agujero!"

    def smokin_that_pack(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Smokin' that Pack!"

    def stop_calling_me_micheal_jordan(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Stop Calling Me Micheal Jordan."

    def you_want_to_go_into_space(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by You Want To Go Into Space?"

    def the_true_warrior(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The True Warrior!"

    def too_lazy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Too Lazy!"

    def literacy_and_corruption(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Literacy and Corruption!"

    def haram(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Haram!"

    def i_am_a_tree(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Am a Tree!"

    def you_want_oil(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by You Want Oil?"

    def slavery_mood(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Slavery Mood!"

    def fortitude_of_europe(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Fortitude of Europe!"

    def kebab_removing_agency(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Kebab Removing Agency!"

    def without_caution_wisdom_is_useless(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Without Caution, Wisdom is Useless…"

    def sri_jayawardenepura_kotte(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Sri Jayawardenepura Kotte!"

    def you_are_the_victim_of_your_own_mistakes(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by You're the Victim of Your Own Mistakes."

    def isnt_tatooine(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Isn't Tatooine"

    def dont_care_about_the_pandemic(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Don't Care about the Pandemic"

    def neutral_in_america(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Neutral in America"

    def double_landlocked(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Double Landlocked"

    def yeah_man_sad_and_poor(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Yeah Man (Sad and Poor)"

    def syrupy_succulence(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Syrupy Succulence"

    def the_home_of_the_sheep(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Home of the Sheep"

    def power_of_chilli(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Power of Chilli"

    def diamonds_diamonds_diamonds(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Diamonds! Diamonds! Diamonds!"

    def we_need_to_build_a_wall(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by We Need to Build a Wall!"

    def terrortorial_expanasion(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Terrortorial Expanasion"

    def eighteen_june_1940(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by 18 June 1940"

    def embrace_our_power(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Embrace Our Power!"

    def we_are_sinking(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by We Are Sinking!!"

    def shipbuilders(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Shipbuilders"

    def meditation(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Meditation"

    def in_coop_we_trust(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by In Coop We Trust"

    def slippy_slopes(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Slippy Slopes"

    def the_power_of_the_shell(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Power of the Shell"

    def unify_italy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Unify Italy!"

    def ruler_of_egypt(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Ruler of Egypt"

    def radiation_detected(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Radiation Detected"

    def three_eyes(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Three Eyes"

    def tonga_time(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Tonga Time"

    def angkor_wat(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Angkor Wat"

    def broken_trident(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Broken Trident"

    def holy_ambitions(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Holy Ambitions"

    def vast_atolls(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Vast Atolls"

    def kebab_protection(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Kebab Protection"

    def brainball(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Brainball"

    def tourists_money_is_mine(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Tourists' Money is Mine"

    def gigachad(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Gigachad"

    def not_free_yet(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Not Free Yet…"

    def brutal_dictatorship(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Brutal Dictatorship"

    def screw_crusaders(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Screw Crusaders!"

    def its_scratching_me(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by It's Scratching Me…"

    def coffin_dance(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Coffin Dance"

    def the_eternal_spring(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Eternal Spring"

    def the_power_of_oil(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Power of Oil"

    def saint_particks_day(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Saint Partick's Day"

    def xbox_ball(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by XBOX Ball"

    def potato_farmer(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Potato Farmer"

    def try_again(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Try Again!"

    def terrorism_everywhere(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Terrorism Everywhere"

    def the_order_of_malta(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Order of Malta"

    def underpopulated(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Underpopulated"

    def save_my_kiwis(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Save My Kiwis"

    def colonized(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Colonized"

    def baby_slavic(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Baby Slavic"

    def voodoo_masters(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Voodoo Masters."

    def i_dont_like_politics(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Don't Like Politics"

    def mine_copper(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Mine Copper"

    def angry_and_rich(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Angry and Rich"

    def london_liberation(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by London Liberation"

    def the_national_dance(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The National Dance"

    def five_hundred_years_stronk(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by 500 Years Stronk!"

    def succession(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Succession"

    def no_army(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by No Army"

    def year_of_rivers(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Year of Rivers"

    def the_taste_of_cashew(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Taste of Cashew"

    def african_democracy(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by African Democracy"

    def postage_stamps(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Postage Stamps"

    def fair_trade(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Fair Trade"

    def rainbow_attack(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Rainbow Attack"

    def this_is_the_home_of_the_brave(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by This Is the Home of the Brave"

    def red_and_black_i_dress_eagle(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Red and Black, I Dress Eagle"

    def the_great_blue_hole(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Great Blue Hole"

    def a_lot_of_memories(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by A Lot of Memories"

    def beep_boop(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Beep Boop"

    def civil_war(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Civil War!"

    def tea_farm(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Tea Farm"

    def im_the_real_congo(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I'm the Real Congo"

    def i_dont_like_my_violent_brother(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Don't Like My Violent Brother!"

    def kill_is_an_art(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Kill is an Art"

    def can_i_into_nordic(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Can I Into Nordic?"

    def absolute_decree(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Absolute Decree"

    def island_hopping(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Island Hopping"

    def i_dont_want_to_be_german(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Don't Want to be German!"

    def river_nation(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by River Nation"

    def tourism_industries(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Tourism Industries"

    def banana_republic(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Banana Republic"

    def ne_mappelez_pas_ivory_coast(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Ne m'appelez pas 'Ivory Coast'"

    def i_refuse_to_join_the_ssr(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Refuse to Join the SSR!"

    def landlocked_communist(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Landlocked Communist"

    def another_explosion(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Another Explosion"

    def europes_child(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Europe's Child"

    def not_vodka_puppet(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Not Vodka Puppet"

    def kingdom_clash(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Kingdom Clash"

    def weapons_lover(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Weapons Lover"

    def rawr(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Rawr!"

    def no_imperialism(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by No Imperialism!"

    def fertility_rate(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Fertility Rate"

    def intifada_until_the_end(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Intifada until the End"

    def humiliated(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Humiliated…"

    def the_mother_colony(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Mother Colony"

    def drive_in_volcano(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Drive in Volcano"

    def pirates_vs_pirates(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Pirates VS Pirates"

    def young_and_already_sad(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Young and already Sad…"

    def very_stable_country(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Very Stable Country"

    def kebab_friends(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Kebab Friends"

    def hakuna_matata(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Hakuna Matata!"

    def i_am_real(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I AM REAL!"

    def dissolution(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Dissolution"

    def green_cape(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Green Cape"

    def diamonds(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Diamonds"

    def isle_of_spice(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Isle of Spice"

    def jellyfish_isle(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Jellyfish Isle"

    def scuba_galore(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Scuba Galore"

    def jewels_of_the_carribean(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Jewels of the Carribean"

    def cannibalism(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Cannibalism"

    def stronk_kebab_remover(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Stronk Kebab Remover"

    def stop_calling_me_qatar(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Stop Calling Me Qatar!"

    def three_sixty_five_beaches(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by 365 Beaches"

    def venice_of_africa(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Venice of Africa"

    def let_the_dragon_be_your_way(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Let the Dragon be Your Way"

    def hunger_games(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Hunger Games"

    def two_capitals(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Two Capitals."

    def countryballs_kart_wii(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Countryballs Kart Wii"

    def perfume_isles(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Perfume Isles"

    def americas_tom_thumb(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by America's Tom Thumb"

    def its_corruption_time(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by It's Corruption Time!"

    def please_make_me_free(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Please Make Me Free"

    def volcanos_awakening(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Volcano's Awakening"

    def the_power_of_water(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Power of Water"

    def im_not_serbian_clay(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I'M NOT SERBIAN CLAY"

    def liberian_ways_of_life(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Liberian Ways of Life"

    def in_the_sky(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by In the Sky"

    def more_companies_than_people(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by More Companies than People"

    def i_like_to_move_it_move_it(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by I Like to Move it Move it"

    def mhajahit_majahapit(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Mhajahit- Majahapit- ?!"

    def smile_for_the_picture(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Smile for the Picture!"

    def home_of_the_dodo(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Home of the Dodo"

    def sleep_on_the_top(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Sleep on the Top"

    def the_floor_is_lava(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by The Floor is Lava"

    def taxes(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Taxes!!"

    def cover_me_in_sunshine(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Cover me in Sunshine"

    def welcome_to_my_canal(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Welcom to My Canal"

    def survivor_season_5(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Survivor: Season 5"

    def vive_la_commune(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Vive La Commune!"

    def cleanliness(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Cleanliness"

    def senegal(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Senegal"

    def come_to_ebola_family(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Come to Ebola Family"

    def pirates(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Pirates!"

    def isnt_a_surname(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Isn't a Surname"

    def portuguese_empires_last_eastern_hope(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Portuguese Empire's Last Eastern Hope"

    def elephant_stampede(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Elephant Stampede"

    def dj_booty(self, target):
        # Implement the ability logic here
        return f"{target.name} is affected by Dj Booty"
    
    def apply(self, target):
        if "damage" in self.description:
            target.hp -= self.power
            return f"{target.name} takes {self.power} damage!"
        elif "heal" in self.description:
            target.hp += self.power
            return f"{target.name} heals {self.power} HP!"
        return f"{target.name} is unaffected."

class Ball:
    def __init__(self, name, hp, atk, abilities):
        self.name = name if name else "Unknown"
        self.hp = hp
        self.atk = atk
        self.abilities = abilities if abilities else []

    def is_alive(self):
        return self.hp > 0

    def choose_action(self):
        return random.choice(self.abilities + ["attack"])

    def attack(self, target):
        damage = random.randint(1, self.atk)
        target.hp -= damage
        return f"{self.name} attacks and deals {damage} damage!"

    def use_ability(self, ability, target):
        return ability.apply(target)

# Read the Excel file
df = pd.read_excel('Abilities.xlsx')

abilities = []
balls_abilities = {}
valid_balls = set(df['BALL'])

# Process the data and store abilities in a dictionary
for index, row in df.iterrows():
    ability = Ability(row['ABILITY NAME'], row['ABILITY'], row['WORTH'])
    if row['BALL'] not in balls_abilities:
        balls_abilities[row['BALL']] = []
    balls_abilities[row['BALL']].append(ability)

decks = {}
