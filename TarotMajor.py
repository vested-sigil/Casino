# TarotMajor.py
major_arcana_cards = [
    'The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor',
    'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit',
    'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance',
    'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun',
    'Judgement', 'The World'
]

major_arcana_interpretations = {
    'The Fool': {
        'upright': ['New beginnings, spontaneity.', 'New relationship.', 'New job opportunity.', 'Fresh health start.'],
        'reversed': ['Holding back, risk-taking.', 'Uncertainty in relationships.', 'Missed job opportunities.', 'Neglecting health.']
    },
    'The Magician': {
        'upright': ['Manifestation, resourcefulness.', 'Power, action.', 'Influence, confidence.', 'Creativity.'],
        'reversed': ['Manipulation, poor planning.', 'Weakness, insecurity.', 'Miscommunication, missed opportunities.', 'Lack of focus.']
    },
    'The High Priestess': {
        'upright': ['Intuition, mystery.', 'Deep emotions, understanding.', 'Trust instincts, hidden talents.', 'Listen to your body.'],
        'reversed': ['Hidden agendas.', 'Secrets in relationships.', 'Ignoring gut feelings.', 'Ignoring health signs.']
    },
    'The Empress': {
        'upright': ['Fertility, femininity.', 'Motherhood, nurturing love.', 'Creativity in work.', 'Physical well-being.'],
        'reversed': ['Dependency, smothering.', 'Neglect in relationships.', 'Creative block.', 'Neglecting self-care.']
    },
    'The Emperor': {
        'upright': ['Authority, structure.', 'Stability in love.', 'Leadership in work.', 'Mental strength.'],
        'reversed': ['Domination, excessive control.', 'Controlling relationship.', 'Misuse of power.', 'Mental stress.']
    },
    'The Hierophant': {
        'upright': ['Spiritual wisdom.', 'Traditional values in love.', 'Mentorship in work.', 'Spiritual health.'],
        'reversed': ['Religious dogma.', 'Stifling relationships.', 'Bad advice.', 'Spiritual misalignment.']
    },
    'The Lovers': {
        'upright': ['Love, harmony.', 'Deep connection.', 'Partnerships in work.', 'Sexual health.'],
        'reversed': ['Imbalance, misalignment.', 'Relationship issues.', 'Work conflicts.', 'Sexual health issues.']
    },
    'The Chariot': {
        'upright': ['Control, willpower.', 'Commitment in love.', 'Achievement in work.', 'Physical discipline.'],
        'reversed': ['Lack of direction.', 'Conflict in love.', 'Lack of ambition.', 'Physical ailments.']
    },
    'Strength': {
        'upright': ['Courage, influence.', 'Inner strength in love.', 'Resilience in work.', 'Emotional strength.'],
        'reversed': ['Inner weakness.', 'Doubt in love.', 'Burnout in work.', 'Emotional fatigue.']
    },
    'The Hermit': {
        'upright': ['Introspection, inner guidance.', 'Solo time in love.', 'Self-reflection in work.', 'Mental health break.'],
        'reversed': ['Isolation.', 'Loneliness in love.', 'Stagnation in work.', 'Mental health issues.']
    },
    'Wheel of Fortune': {
        'upright': ['Good luck, destiny.', 'Fateful meeting in love.', 'Opportunities in work.', 'Positive health cycle.'],
        'reversed': ['Bad luck, resistance to change.', 'Fateful separation in love.', 'Missed opportunities.', 'Negative health cycle.']
    },
    'Justice': {
        'upright': ['Fairness, truth.', 'Balance in love.', 'Legal matters in work.', 'Balance in health.'],
        'reversed': ['Unfairness, lack of accountability.', 'Injustice in love.', 'Legal issues in work.', 'Health imbalances.']
    },
    'The Hanged Man': {
        'upright': ['Pause, surrender.', 'Letting go in love.', 'Sacrifice in work.', 'Health introspection.'],
        'reversed': ['Stalling, needless sacrifice.', 'Clinginess in love.', 'Fear of sacrifice in work.', 'Ignoring health signs.']
    },
    'Death': {
        'upright': ['Endings, transformation.', 'End of a relationship phase.', 'End of a work phase.', 'Transformation in health.'],
        'reversed': ['Fear of change.', 'Fear of ending in love.', 'Stagnation in work.', 'Fear of health change.']
    },
    'Temperance': {
        'upright': ['Balance, moderation.', 'Harmony in love.', 'Work-life balance.', 'Health balance.'],
        'reversed': ['Imbalance, excess.', 'Imbalance in love.', 'Work-life conflict.', 'Health extremes.']
    },
    'The Devil': {
        'upright': ['Bondage, addiction.', 'Toxic love.', 'Work addiction.', 'Health neglect.'],
        'reversed': ['Breaking free.', 'Breaking toxic bonds in love.', 'Breaking work chains.', 'Health recovery.']
    },
    'The Tower': {
        'upright': ['Sudden upheaval.', 'Sudden breakup.', 'Work collapse.', 'Health crisis.'],
        'reversed': ['Fear of change.', 'Avoiding breakup.', 'Avoiding work change.', 'Avoiding health issues.']
    },
    'The Star': {
        'upright': ['Hope, inspiration.', 'Rejuvenated love.', 'Work inspiration.', 'Health recovery.'],
        'reversed': ['Despair, lack of faith.', 'Hopelessness in love.', 'Lack of inspiration in work.', 'Health despair.']
    },
    'The Moon': {
        'upright': ['Illusion, intuition.', 'Dreams in love.', 'Intuition in work.', 'Listening to the body.'],
        'reversed': ['Confusion, deception.', 'Deception in love.', 'Misunderstandings in work.', 'Ignoring body signs.']
    },
'The Sun': {
        'upright': ['Success, joy.', 'Happiness in love.', 'Work success.', 'Vibrant health.'],
        'reversed': ['Temporary setbacks.', 'Temporary love issues.', 'Work setbacks.', 'Health setbacks.']
    },
    'Judgement': {
        'upright': ['Reckoning, awakening.', 'Making amends in love.', 'New job opportunities.', 'Health awakening.'],
        'reversed': ['Self-doubt.', 'Avoiding love amends.', 'Missed job opportunities.', 'Health avoidance.']
    },
    'The World': {
        'upright': ['Completion, integration.', 'Wholeness in love.', 'Career fulfillment.', 'Health achievement.'],
        'reversed': ['Lack of closure.', 'Love detachment.', 'Career stagnation.', 'Health dissatisfaction.']
    }
}

# Functions to get card interpretations
def get_major_arcana_interpretation(card, orientation):
    card = card.strip()
    if card in major_arcana_interpretations:
        if orientation == 'upright':
            return major_arcana_interpretations[card]['upright']
    elif orientation == 'reversed':
            return major_arcana_interpretations[card]['reversed']
    return ["Invalid card or orientation."]


card = 'The Fool'
orientation = 'upright' or 'reversed'
interpretation = get_major_arcana_interpretation(card, orientation)
print(interpretation)
print(card)
