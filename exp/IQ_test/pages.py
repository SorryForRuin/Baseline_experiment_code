from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class IQ_test1(Page):
    form_model = "player"
    form_fields = ["answer_entered1"]


    def before_next_page(self):
        if Constants.correct_answer1 == self.player.answer_entered1:
            self.player.score1 = Constants.payment_per_correct_answer

class IQ_test2(Page):
    form_model = "player"
    form_fields = ["answer_entered2"]

    def before_next_page(self):
        if Constants.correct_answer2 == self.player.answer_entered2:
            self.player.score2 += Constants.payment_per_correct_answer

class IQ_test3(Page):
    form_model = "player"
    form_fields = ["answer_entered3"]

    def before_next_page(self):
        if Constants.correct_answer3 == self.player.answer_entered3:
            self.player.score3 += Constants.payment_per_correct_answer

class IQ_test4(Page):
    form_model = "player"
    form_fields = ["answer_entered4"]

    def before_next_page(self):
        if Constants.correct_answer4 == self.player.answer_entered4:
            self.player.score4 += Constants.payment_per_correct_answer

class IQ_test5(Page):
    form_model = "player"
    form_fields = ["answer_entered5"]

    def before_next_page(self):
        if Constants.correct_answer5 == self.player.answer_entered5:
            self.player.score5 += Constants.payment_per_correct_answer

class IQ_test6(Page):
    form_model = "player"
    form_fields = ["answer_entered6"]

    def before_next_page(self):
        if Constants.correct_answer6 == self.player.answer_entered6:
            self.player.score6 += Constants.payment_per_correct_answer

class IQ_test7(Page):
    form_model = "player"
    form_fields = ["answer_entered7"]

    def before_next_page(self):
        if Constants.correct_answer7 == self.player.answer_entered7:
            self.player.score7 += Constants.payment_per_correct_answer

class IQ_test8(Page):
    form_model = "player"
    form_fields = ["answer_entered8"]

    def before_next_page(self):
        if Constants.correct_answer8 == self.player.answer_entered8:
            self.player.score8 += Constants.payment_per_correct_answer

class IQ_test9(Page):
    form_model = "player"
    form_fields = ["answer_entered9"]

    def before_next_page(self):
        if Constants.correct_answer9 == self.player.answer_entered9:
            self.player.score9 += Constants.payment_per_correct_answer

class IQ_test10(Page):
    form_model = "player"
    form_fields = ["answer_entered10"]

    def before_next_page(self):
        if Constants.correct_answer10 == self.player.answer_entered10:
            self.player.score10 += Constants.payment_per_correct_answer

class ResultsWaitPage(WaitPage):
    form_model = "player"



    # group_by_arrival_time = True
    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        current_player = self.player.id_in_group

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            other_players = set(self.group.get_players())
            other_players.remove(p)
            p2, p3, p4 = random.sample(other_players, 3)
            resP = p.score1 + p.score2 + p.score3 + p.score4 + p.score5 + p.score6 + p.score7 + p.score8 + p.score9 + p.score10
            resP2 = p2.score1 + p2.score2 + p2.score3 + p2.score4 + p2.score5 + p2.score6 + p2.score7 + p2.score8 + p2.score9 + p2.score10
            resP3 = p3.score1 + p3.score2 + p3.score3 + p3.score4 + p3.score5 + p3.score6 + p3.score7 + p3.score8 + p3.score9 + p3.score10
            resP4 = p4.score1 + p4.score2 + p4.score3 + p4.score4 + p4.score5 + p4.score6 + p4.score7 + p4.score8 + p4.score9 + p4.score10

            if resP > resP2:
                p.NFresult1 = 2
            elif resP == resP2:
                p.NFresult1 = 1
            elif resP < resP2:
                p.NFresult1 = 0

            if resP > resP3:
                p.NFresult2 = 2
            elif resP == resP3:
                p.NFresult2 = 1
            elif resP < resP3:
                p.NFresult2 = 0

            if resP > resP4:
                p.NFresult3 = 2
            elif resP == resP4:
                p.NFresult3 = 1
            elif resP < resP4:
                p.NFresult3 = 0
    # def after_all_players_arrive(self):
    #     results = dict()
    #     for i, p in enumerate(self.group.get_players()):
    #         results[p] = p.score1 + p.score2 + p.score3 + p.score4 + p.score5 + p.score6 + p.score7 + p.score8 + p.score9 + p.score10
    #     # player1, player2, player3, player4 = self.group.get_players()
    #     # player3, player4, player5, player6, player7, player8, player9, player10 = self.group.get_players()
    #     # for p in self.group.get_players():
    #     #     pass
    #     player_set = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"]
    #     noisy_feedback1 = random.choice(player_set)
    #     noisy_feedback2 = random.choice(player_set)
    #     noisy_feedback3 = random.choice(player_set)
    #     for p1 in results.keys():
    #         for i, p2 in enumerate(results.keys()):
    #             pass
    #
    #     id_set = [1, 2, 3, 4]
    #
    #
    #     # while noisy_feedback1 == current_player:
    #     #     noisy_feedback1 = random.choice(player_set)
    #     #
    #     # while noisy_feedback2 == current_player or noisy_feedback2 == noisy_feedback1:
    #     #     noisy_feedback2 = random.choice(player_set)
    #     #
    #     # while noisy_feedback3 == current_player or noisy_feedback3 == noisy_feedback1 or noisy_feedback3 == noisy_feedback2:
    #     #     noisy_feedback3 = random.choice(player_set)
    #
    #     # noisy feedback first round
    #     # for x in player_set:
    #     #     if noisy_feedback1 == player1:
    #     #         if self.player.combined_score > player1.combined_score:
    #     #             self.player.NFresult1 = 2
    #     #         if self.player.combined_score == player1.combined_score:
    #     #             self.player.NFresult1 = 1
    #     #         if self.player.combined_score < player1.combined_score:
    #     #             self.player.NFresult1 = 0
    #     #     if noisy_feedback1 == player2:
    #     #         if self.player.combined_score > player2.combined_score:
    #     #             self.player.NFresult1 = 2
    #     #         if self.player.combined_score == player2.combined_score:
    #     #             self.player.NFresult1 = 1
    #     #         if self.player.combined_score < player2.combined_score:
    #     #             self.player.NFresult1 = 0
    #     #     if noisy_feedback1 == player3:
    #     #         if self.player.combined_score > player3.combined_score:
    #     #             self.player.NFresult1 = 2
    #     #         if self.player.combined_score == player3.combined_score:
    #     #             self.player.NFresult1 = 1
    #     #         if self.player.combined_score < player3.combined_score:
    #     #             self.player.NFresult1 = 0
    #     #     if noisy_feedback1 == player3:
    #     #         if self.player.combined_score > player4.combined_score:
    #     #             self.player.NFresult1 = 2
    #     #         if self.player.combined_score == player4.combined_score:
    #     #             self.player.NFresult1 = 1
    #     #         if self.player.combined_score < player4.combined_score:
    #     #             self.player.NFresult1 = 0
    #     #     if noisy_feedback2 == player1:
    #     #         if self.player.combined_score > player1.combined_score:
    #     #             self.player.NFresult2 = 2
    #     #         if self.player.combined_score == player1.combined_score:
    #     #             self.player.NFresult2 = 1
    #     #         if self.player.combined_score < player1.combined_score:
    #     #             self.player.NFresult2 = 0
    #     #     if noisy_feedback2 == player2:
    #     #         if self.player.combined_score > player2.combined_score:
    #     #             self.player.NFresult2 = 2
    #     #         if self.player.combined_score == player2.combined_score:
    #     #             self.player.NFresult2 = 1
    #     #         if self.player.combined_score < player2.combined_score:
    #     #             self.player.NFresult2 = 0
    #     #     if noisy_feedback2 == player3:
    #     #         if self.player.combined_score > player3.combined_score:
    #     #             self.player.NFresult2 = 2
    #     #         if self.player.combined_score == player3.combined_score:
    #     #             self.player.NFresult2 = 1
    #     #         if self.player.combined_score < player3.combined_score:
    #     #             self.player.NFresult2 = 0
    #     #     if noisy_feedback2 == player4:
    #     #         if self.player.combined_score > player4.combined_score:
    #     #             self.player.NFresult2 = 2
    #     #         if self.player.combined_score == player4.combined_score:
    #     #             self.player.NFresult2 = 1
    #     #         if self.player.combined_score < player4.combined_score:
    #     #             self.player.NFresult2 = 0
    #     #     if noisy_feedback3 == player1:
    #     #         if self.player.combined_score > player1.combined_score:
    #     #             self.player.NFresult3 = 2
    #     #         if self.player.combined_score == player1.combined_score:
    #     #             self.player.NFresult3 = 1
    #     #         if self.player.combined_score < player1.combined_score:
    #     #             self.player.NFresult3 = 0
    #     #     if noisy_feedback3 == player2:
    #     #         if self.player.combined_score > player2.combined_score:
    #     #             self.player.NFresult3 = 2
    #     #         if self.player.combined_score == player2.combined_score:
    #     #             self.player.NFresult3 = 1
    #     #         if self.player.combined_score < player2.combined_score:
    #     #             self.player.NFresult3 = 0
    #     #     if noisy_feedback3 == player3:
    #     #         if self.player.combined_score > player3.combined_score:
    #     #             self.player.NFresult3 = 2
    #     #         if self.player.combined_score == player3.combined_score:
    #     #             self.player.NFresult3 = 1
    #     #         if self.player.combined_score < player3.combined_score:
    #     #             self.player.NFresult3 = 0
    #     #     if noisy_feedback3 == player4:
    #     #         if self.player.combined_score > player4.combined_score:
    #     #             self.player.NFresult3 = 2
    #     #         if self.player.combined_score == player4.combined_score:
    #     #             self.player.NFresult3 = 1
    #     #         if self.player.combined_score < player4.combined_score:
    #     #             self.player.NFresult3 = 0


class Feedback(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True



class FeedbackAgain(Page):
    def is_displayed(self):
        if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
            return False
        else:
            return True
class Results(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True

        if self.participant.vars["failed_check"] == False:
            return False
        else:
            return True


class Confirm(Page):
    form_model = "player"
    form_fields = ["ConfirmQ1", "ConfirmQ2", "ConfirmQ3"]

    def is_displayed(self):

        if self.round_number == 1:
            return True


    def before_next_page(self):

        if self.player.ConfirmQ1 == "I have performed BETTER than that player":
            if self.player.NFresult1 == 2:
                self.player.confirm_check1 = False
            else:
                self.player.confirm_check1 = True
        if self.player.ConfirmQ1 == "I have performed IDENTICALLY compared to that player that player":
            if self.player.NFresult1 == 1:
                self.player.confirm_check1 = False
            else:
                self.player.confirm_check1 = True
        if self.player.ConfirmQ1 == "I have performed WORSE than that player":
            if self.player.NFresult1 == 0:
                self.player.confirm_check1 = False
            else:
                self.player.confirm_check1 = True

        if self.player.ConfirmQ2 == "I have performed BETTER than that player":
            if self.player.NFresult2 == 2:
                self.player.confirm_check2 = False
            else:
                self.player.confirm_check2 = True
        if self.player.ConfirmQ2 == "I have performed IDENTICALLY compared to that player that player":
            if self.player.NFresult2 == 1:
                self.player.confirm_check2 = False
            else:
                self.player.confirm_check2 = True
        if self.player.ConfirmQ2 == "I have performed WORSE than that player":
            if self.player.NFresult2 == 0:
                self.player.confirm_check2 = False
            else:
                self.player.confirm_check2 = True

        if self.player.ConfirmQ3 == "I have performed BETTER than that player":
            if self.player.NFresult3 == 2:
                self.player.confirm_check3 = False
            else:
                self.player.confirm_check3 = True
        if self.player.ConfirmQ3 == "I have performed IDENTICALLY compared to that player that player":
            if self.player.NFresult3 == 1:
                self.player.confirm_check3 = False
            else:
                self.player.confirm_check3 = True
        if self.player.ConfirmQ3 == "I have performed WORSE than that player":
            if self.player.NFresult3 == 0:
                self.player.confirm_check3 = False
            else:
                self.player.confirm_check3 = True


        if self.player.confirm_check1 is True or self.player.confirm_check1 is True or self.player.confirm_check1 is True:
            self.participant.vars["failed_check"] = True
        else:
            self.participant.vars["failed_check"] = False


class ConfirmAgain(Page):
    form_model = "player"
    form_fields = ["ConfirmQ1", "ConfirmQ2", "ConfirmQ3"]

    def is_displayed(self):
        if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
            return False
        else:
            return True

    def before_next_page(self):

        if self.player.ConfirmQ1 == "I have performed BETTER than that player":
            if self.player.NFresult1 == 2:
                self.player.confirm_check1 = False
            else:
                self.player.confirm_check1 = True
        if self.player.ConfirmQ1 == "I have performed IDENTICALLY compared to that player that player":
            if self.player.NFresult1 == 1:
                self.player.confirm_check1 = False
            else:
                self.player.confirm_check1 = True
        if self.player.ConfirmQ1 == "I have performed WORSE than that player":
            if self.player.NFresult1 == 0:
                self.player.confirm_check1 = False
            else:
                self.player.confirm_check1 = True

        if self.player.ConfirmQ2 == "I have performed BETTER than that player":
            if self.player.NFresult2 == 2:
                self.player.confirm_check2 = False
            else:
                self.player.confirm_check2 = True
        if self.player.ConfirmQ2 == "I have performed IDENTICALLY compared to that player that player":
            if self.player.NFresult2 == 1:
                self.player.confirm_check2 = False
            else:
                self.player.confirm_check2 = True
        if self.player.ConfirmQ2 == "I have performed WORSE than that player":
            if self.player.NFresult2 == 0:
                self.player.confirm_check2 = False
            else:
                self.player.confirm_check2 = True

        if self.player.ConfirmQ3 == "I have performed BETTER than that player":
            if self.player.NFresult3 == 2:
                self.player.confirm_check3 = False
            else:
                self.player.confirm_check3 = True
        if self.player.ConfirmQ3 == "I have performed IDENTICALLY compared to that player that player":
            if self.player.NFresult3 == 1:
                self.player.confirm_check3 = False
            else:
                self.player.confirm_check3 = True
        if self.player.ConfirmQ3 == "I have performed WORSE than that player":
            if self.player.NFresult3 == 0:
                self.player.confirm_check3 = False
            else:
                self.player.confirm_check3 = True

        if self.player.confirm_check1 is True or self.player.confirm_check1 is True or self.player.confirm_check1 is True:
            self.participant.vars["failed_check"] = True
        else:
            self.participant.vars["failed_check"] = False
class FailCheck(Page):
    def is_displayed(self):
        if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
            return False
        else:
            return True
class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        return {
            "combined_payoff":self.player.combined_score
        }
class Likelihood1(Page):
    form_model = "player"
    form_fields = ["likelihood1"]
    # def vars_for_template(self):
    #     self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
    #     if self.player.combined_score >= 5:
    #         self.player.payoff1 = Constants.fix_payment + Constants.variable_payment_coef * (1-self.player.likelihood1//100)
    #     else:
    #         self.player.payoff1 = Constants.fix_payment + Constants.variable_payment_coef * (0 - self.player.likelihood1 // 100)
    #     return {
    #         "payoff1":self.player.payoff1
    #     }
class Likelihood2(Page):
    form_model = "player"
    form_fields = ["likelihood2"]
    def is_displayed(self):
        if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
            return True
        else:
            return False
    # def vars_for_template(self):
    #     self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
    #     if self.player.combined_score >= 5:
    #         self.player.payoff2 = Constants.fix_payment + Constants.variable_payment_coef * (1-self.player.likelihood2//100)
    #     else:
    #         self.player.payoff2 = Constants.fix_payment + Constants.variable_payment_coef * (0 - self.player.likelihood2 // 100)
    #     payoff_set = [self.player.payoff1, self.player.payoff2]
    #     self.player.actual_payoff = random.choice(payoff_set)
    #
    #     return {
    #         "actual_payoff":self.player.actual_payoff
    #     }
class SurveyQuestions(Page):
    form_model = "player"
    form_fields = ["gender", "age", "education", "employment", "marriage"]
    def is_displayed(self):
        if self.player.confirm_check1 is False and self.player.confirm_check2 is False and self.player.confirm_check3 is False:
            return True
        else:
            return False

page_sequence = [IQ_test1, IQ_test2, IQ_test3, IQ_test4, IQ_test5, IQ_test6,
                 IQ_test7, IQ_test8, IQ_test9, IQ_test10, ResultsWaitPage,
                 Likelihood1, Feedback, Confirm, FailCheck, FeedbackAgain, ConfirmAgain, Likelihood2, SurveyQuestions ]
