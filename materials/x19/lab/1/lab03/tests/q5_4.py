test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(average_20th_century_rating - 8.280113636363636) < 1e-2
          True
          >>> abs(average_21st_century_rating - 8.23108108108108) < 1e-2
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
